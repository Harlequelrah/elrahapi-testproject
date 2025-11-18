from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from settings.auth.configs import authentication_router,authentication
from settings.auth.routers import user_router

# from myapp.router import myapp_router
from settings.database import database

from fastapi import FastAPI

app = FastAPI(root_path="/api")

app.include_router(authentication_router)
app.include_router(user_router)


@app.get("/")
async def hello():
    return {"message": "hello"}


# app.include_router(myapp_router)
app.add_middleware(
    ErrorHandlingMiddleware,
)
