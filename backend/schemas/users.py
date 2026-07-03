from pydantic import BaseModel, Field
from pydantic import ConfigDict

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    role: str = "Candidate"

    model_config = ConfigDict(populate_by_name=True)

class UserCreate(UserBase):
    pass

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str

    model_config = ConfigDict(from_attributes=True)

class Login_User(BaseModel):
    email: str
    password: str