from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src import models

from .database import engine, get_db
from .schemas import User, UserCreate
from .services import create_user, get_user_by_id, get_user_list

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get('/users/', response_model=List[User])
def get_users(db: Session = Depends(get_db)) -> List[User]:
    return get_user_list(db)


@router.get('/users/{user_id}/', response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    return get_user_by_id(db, user_id)


@router.post('/users/', response_model=User)
def post_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    return create_user(user=user, db=db)
