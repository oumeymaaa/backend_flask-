import datetime

from bson.objectid import ObjectId



def bson_to_json(ourBson: dict):
     new_object: dict = {}
     for key, value in ourBson.items():
          if type(value) is ObjectId or type(value) is datetime.datetime:
               new_object[key] = str(value)
          else:
               new_object[key] = value
     return new_object


