from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    fullname: str
    password: str

class UserCreateRequest(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # Enables ORM mode for Pydantic
