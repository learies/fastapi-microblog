from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database import get_db

from .schemas import User, UserCreate
from .services import (create_user, get_user_by_id, get_user_by_username,
                       get_user_list)

router = APIRouter()


@router.get('/users/', response_model=list[User])
def get_users(db: Session = Depends(get_db)) -> list[User]:
    return get_user_list(db)


@router.get(
    '/users/{user_id}/', response_model=User, status_code=status.HTTP_200_OK
)
def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    if not get_user_by_id(db, user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Пользователя по `id {user_id}` не существует.',
        )
    return get_user_by_id(db, user_id)


@router.post(
    '/users/', response_model=User, status_code=status.HTTP_201_CREATED
)
def post_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Пользователь с именем `{user.username}` уже существует.',
        )
    return create_user(user=user, db=db)
