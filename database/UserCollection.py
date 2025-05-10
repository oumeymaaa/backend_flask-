from enum import StrEnum

class UserCollection(StrEnum):
    USERNAME = 'username'
    PASSWORD = 'password'
    EMAIL = 'email'
    PHONE_NUMBER = 'phone_number'
    FULL_NAME = 'full_name'
    LAST_LOGIN = 'last_login'
    LOGIN_COUNT = 'login_count'
    ACTIVATE_AT = 'activate_at'
    IS_ACTIVE_PREMIER = 'is_active_premium'

