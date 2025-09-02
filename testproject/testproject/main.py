from fastapi import FastAPI
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware

# from myapp.router import app_myapp
from elrahapi.middleware.middleware_helper import MiddlewareHelper
from settings.database import database
from settings.auth.routers import user_router, role_router
from settings.auth.configs import authentication_router

app = FastAPI(root_path="/api")


@app.get("/")
async def hello():
    return {"message": "hello"}


app.include_router(user_router)
app.include_router(role_router)
app.include_router(authentication_router)

# app.include_router(app_myapp)
middleware_helper = MiddlewareHelper()
app.add_middleware(ErrorHandlingMiddleware, middleware_helper=middleware_helper)
