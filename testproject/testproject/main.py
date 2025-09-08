from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware

# from myapp.router import app_myapp
from elrahapi.middleware.middleware_helper import MiddlewareHelper
from settings.auth.configs import authentication_router
from settings.auth.routers import role_router, user_router

from settings.database import database
from task.router import task_router

from fastapi import FastAPI

app = FastAPI(root_path="/api")


@app.get("/")
async def hello():
    return {"message": "hello"}


app.include_router(user_router)
# app.include_router(role_router)
app.include_router(authentication_router)
app.include_router(task_router)
# app.include_router(app_myapp)
app.add_middleware(ErrorHandlingMiddleware)
