from enum import StrEnum

class NotificationCollection(StrEnum):
    USER_ID = 'user_id'
    CATEGORY = 'category'
    TITLE = 'title'
    BODY = 'body'
    DATA = 'data'
    CREATED_AT = 'created_at'  
    UPDATED_AT = 'updated_at'