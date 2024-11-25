from pydantic import BaseModel


class ResponseTokenLoginSchema(BaseModel):
    access_token: str
    refresh_token: str