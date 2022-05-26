from fastapi import FastAPI

from .routers import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


app: FastAPI = create_app()
