from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id: int = None

    class Config:
        orm_mode = True


class UserBaseInDB(UserBase):
    username: str
    email: EmailStr


class UserCreate(UserBaseInDB):
    password: str
    email: EmailStr


class UserInDB(UserBaseInDB):
    hashed_password: str


class User(UserBaseInDB):
    is_active: bool
