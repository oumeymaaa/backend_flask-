from enum import StrEnum

from pydantic import BaseModel

class TokenActivateModelFields(StrEnum):
    email = 'email'
    code = 'code'



class TokenActivateModel(BaseModel):
    email: str
    code: str