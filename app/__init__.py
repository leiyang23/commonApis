from fastapi import FastAPI

from app.apis import tool_router


def get_app():
    app = FastAPI()
    app.include_router(tool_router)
    return app
