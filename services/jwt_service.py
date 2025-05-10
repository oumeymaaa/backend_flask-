import datetime

from flask_jwt_extended import create_access_token, create_refresh_token


def app_create_access_token(identity: str, claims: dict[str, str | int] | None = None):
    return create_access_token(identity=identity, expires_delta=datetime.timedelta(hours=1))

def app_create_refresh_token(identity: str):
    # one week should be ok
    return create_refresh_token(identity=identity, expires_delta=datetime.timedelta(days=7))
