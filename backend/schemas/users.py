from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str
    email: str
    password: str
    role: str

class UserCreate(UserBase):
    pass

class UserResponse(BaseModel):
    id: int
    name: str = Field(..., alias="username")
    email: str
    role: str

    class Config:
        from_attributes = True
        allow_population_by_field_name = True

class Login_User(BaseModel):
    email: str
    password: str