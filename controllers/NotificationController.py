from flasgger import swag_from
from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from model.NotificationModel import NotificationModel
from database import databaseInstance
import requests
import json

notification_bp = Blueprint('notification', __name__)

EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"

def send_push_notification(token, message):
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        "to": token,
        "title": message.get("title"),
        "body": message.get("body"),
        "data": message.get("data"),
    }

    response = requests.post(EXPO_PUSH_URL, json=payload, headers=headers)
    return response.json()




@notification_bp.route('/send_notification', methods=['POST'])
@swag_from({
    'tags': ['Notifications'],
    'summary': 'Send a push notification',
    'description': 'Sends a categorized push notification and stores it in the database.',
    'consumes': ['application/json'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'token': {
                        'type': 'string',
                        'example': 'fcm_token_here'
                    },
                    'category': {
                        'type': 'string',
                        'enum': ['distraction_alert', 'physical_alert', 'mental_alert'],
                        'example': 'distraction_alert'
                    },
                    'user_id': {
                        'type': 'string',
                        'example': 'user_12345'
                    }
                },
                'required': ['token', 'category']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Notification sent successfully',
            'schema': {
                'type': 'object',
                'example': {'success': True, 'message': 'Notification sent'}
            }
        },
        400: {
            'description': 'Invalid request body or data',
            'schema': {
                'type': 'object',
                'example': {'error': 'Token and category are required'}
            }
        }
    }
})
def send_notification():
    """
        @data:
            -token: str
            -category: enum(distraction_alert, physical_alert, mental_alert)
            -user_id
    """
    data = request.json
    token = data.get('token')
    category = data.get('category')

    print(data)
    print(token) 
    print(category) 
    print(data.get('user_id'))
    if not token or not category:
        return jsonify({"error": "Token and category are required"}), 400

    # Logique de notification basée sur la catégorie
    messages = {
        "distraction_alert": {
            "title": "🚨 Distraction Alert",
            "body": "Vous êtes distrait. Faites attention à la route !",
            "data": {"category": "distraction_alert"}
        },
        "physical_alert": {
            "title": "⚠️ Physical Condition Alert",
            "body": "Prenez une pause, votre état physique nécessite de l'attention.",
            "data": {"category": "physical_alert"}
        },
        "mental_alert": {
            "title": "🔔 Mental Condition Alert",
            "body": "Prenez une pause, votre état mental nécessite de l'attention.",
            "data": {"category": "mental_alert"}
        }
    }

    message = messages.get(category, {"title": "General Alert", "body": "You have a new notification", "data": {"category": "general"}})

    # Envoi de la notification push
    result = send_push_notification(token, message)

    # Enregistrement de la notification dans la base de données
    user_id = data.get("user_id")  # Assure-toi que l'ID utilisateur est passé dans la requête
    if user_id:
        try:
            # Créer et enregistrer la notification dans la base de données MongoDB
            notification = NotificationModel(
                user_id=user_id,
                category=category,
                title=message["title"],
                body=message["body"],
                data=message["data"]
            )
            notification.timestamp_snapshot()  # Met à jour les timestamps
            databaseInstance.db.notifications.insert_one(notification.dict())  # Enregistre dans MongoDB
        except ValidationError as e:
            return jsonify({"error": "Invalid notification data", "details": str(e)}), 400

    return jsonify(result)

@notification_bp.route('/user_notifications', methods=['GET'])
@swag_from({
    'tags': ['Notifications'],
    'summary': 'Get user notifications',
    'description': 'Fetch a paginated list of notifications for a specific user.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'The ID of the user to fetch notifications for',
            'example': 'user_12345'
        },
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 1,
            'description': 'The page number for pagination'
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 10,
            'description': 'The number of notifications per page'
        }
    ],
    'responses': {
        200: {
            'description': 'List of user notifications',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        '_id': {'type': 'string', 'example': '661f854b5c2b4fef3dc3d4e0'},
                        'user_id': {'type': 'string', 'example': 'user_12345'},
                        'category': {'type': 'string', 'example': 'distraction_alert'},
                        'title': {'type': 'string', 'example': '🚨 Distraction Alert'},
                        'body': {'type': 'string', 'example': 'Vous êtes distrait. Faites attention à la route !'},
                        'data': {'type': 'object', 'example': {'category': 'distraction_alert'}},
                        'created_at': {'type': 'string', 'format': 'date-time'},
                        'updated_at': {'type': 'string', 'format': 'date-time'}
                    }
                }
            }
        },
        400: {
            'description': 'Missing or invalid parameters',
            'schema': {
                'type': 'object',
                'example': {'error': 'User ID is required'}
            }
        }
    }
})
def get_user_notifications():
    user_id = request.args.get('user_id')  # Récupérer l'ID utilisateur via les paramètres de l'URL
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    # Pagination (optionnelle)
    page = int(request.args.get('page', 1))  # Page par défaut = 1
    limit = int(request.args.get('limit', 10))  # Limite par défaut = 10 notifications par page
    skip = (page - 1) * limit

    # Récupération des notifications de l'utilisateur
    notifications = list(databaseInstance.db.notifications.find({"user_id": user_id}).skip(skip).limit(limit))

    # Transformer les résultats pour les renvoyer sous un format JSON valide
    for notification in notifications:
        notification["_id"] = str(notification["_id"])  # Convertir l'ObjectId en string pour le JSON

    return jsonify(notifications)

