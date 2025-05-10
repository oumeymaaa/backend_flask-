import datetime
from pydantic import BaseModel
from typing import Optional
from model.BaseModelModule import BaseModelApp


# class UserUpdateDto(BaseModel):
#     full_name: Optional[str] = None
#     phone_number: Optional[str] = None



class UserSignUpDto(BaseModelApp):
    full_name: str
    phone_number: str
    username: str
    email: str
    password: str

class UpdateUserModel(BaseModel):
    full_name: str
    phone_number: str

class UserAdditionalInfo(UserSignUpDto):
    last_signin: Optional[datetime.datetime]
    signin_count: int = 0


class SignInDto(BaseModel):
    email: str
    password: str
