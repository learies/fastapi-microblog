from fastapi import FastAPI

from .database import engine
from .models import Base
from .routers import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    Base.metadata.create_all(bind=engine)
    return app


app: FastAPI = create_app()
