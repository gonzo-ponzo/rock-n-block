from fastapi import FastAPI
from fastapi.routing import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise


from config import IP_SERVER, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from tokens.routes import tokens_api_router

openapi_tags = [
    {
        "name": "Tokens",
        "description": "Token routes",
    },
]
app = FastAPI(title="rock-n-block", openapi_tags=openapi_tags)

origins = [
    "http://localhost:3000",
    "https://127.0.0.1:3000",
    "http://127.0.0.1:3000",
    f"{IP_SERVER}",
    f"https://{IP_SERVER}",
    f"http://{IP_SERVER}",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

router = APIRouter(prefix="/api/v1")
router.include_router(tokens_api_router, tags=["Tokens"])
app.include_router(router)

register_tortoise(
    app,
    db_url=f"{DB_USER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    modules={"models": ["db.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
