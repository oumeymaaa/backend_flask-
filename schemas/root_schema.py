
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "My API",
        "description": "API for user authentication",
        "version": "1.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "scheme": "bearer",
            "name": "Authorization",
            'bearerFormat': 'JWT',
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: **Bearer {token}**"
        }
    },
    "components": {
        "schemas": {
            "UserSignUpDto": {
                "type": "object",
                "properties": {
                    "full_name": {"type": "string", "example": "John Doe"},
                    "phone_number": {"type": "string", "example": "+1234567890"},
                    "username": {"type": "string", "example": "johndoe"},
                    "email": {"type": "string", "format": "email", "example": "john@example.com"},
                    "password": {"type": "string", "example": "SecurePass123"}
                },
                "required": ["full_name", "phone_number", "username", "email", "password"]
            },
            "UpdateUserModel": {
                "type": "object",
                "properties": {
                    "full_name": {"type": "string", "example": "John Updated"},
                    "phone_number": {"type": "string", "example": "+1234567890"}
                },
                "required": ["full_name", "phone_number"]
            },
            "UserAdditionalInfo": {
                "type": "object",
                "properties": {
                    "full_name": {"type": "string", "example": "John Doe"},
                    "phone_number": {"type": "string", "example": "+1234567890"},
                    "username": {"type": "string", "example": "johndoe"},
                    "email": {"type": "string", "format": "email", "example": "john@example.com"},
                    "password": {"type": "string", "example": "SecurePass123"},
                    "last_signin": {"type": "string", "format": "date-time", "example": "2024-01-01T12:00:00Z"},
                    "signin_count": {"type": "integer", "default": 0}
                },
                "required": ["full_name", "phone_number", "username", "email", "password"]
            },
            "SignInDto": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "format": "email", "example": "john@example.com"},
                    "password": {"type": "string", "example": "SecurePass123"}
                },
                "required": ["email", "password"]
            },
            "NotificationModel": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "example": "user123"},
                    "category": {"type": "string", "example": "alert"},
                    "title": {"type": "string", "example": "Your account has been updated"},
                    "body": {"type": "string", "example": "We have updated your account details."},
                    "data": {
                        "type": "object",
                        "additionalProperties": {
                            "type": "string",
                            "example": "extra info"
                        }
                    },
                    "created_at": {"type": "string", "format": "date-time", "example": "2024-01-01T12:00:00Z"},
                    "updated_at": {"type": "string", "format": "date-time", "example": "2024-01-01T12:00:00Z"}
                },
                "required": ["user_id", "category", "title", "body", "data"]
            },
            "TokenModel": {
                "type": "object",
                "properties": {
                    "access_token": {"type": "string", "example": "access-token-example"},
                    "refresh_token": {"type": "string", "example": "refresh-token-example"}
                },
                "required": ["access_token", "refresh_token"]
            },
            "Message": {
               "type": "object",
               "properties": {
                   "message": {"type": "string", "example": "hello there"}
               },
               "required": ["message"]
            }
        }
    }
}
