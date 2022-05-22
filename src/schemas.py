from pydantic import BaseModel


class UserBase(BaseModel):
    id: int = None

    class Config:
        orm_mode = True


class UserBaseInDB(UserBase):
    username: str


class UserCreate(UserBaseInDB):
    password: str


class UserInDB(UserBaseInDB):
    hashed_password: str


class User(UserBaseInDB):
    pass
