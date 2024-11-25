from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
    user_name: str = Field(..., max_length=30)
    password: str = Field(..., min_length=8)