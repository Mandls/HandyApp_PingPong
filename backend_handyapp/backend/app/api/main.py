from fastapi import APIRouter

from app.api.routes import matches

api_router = APIRouter()

api_router.include_router(matches.router, prefix="/matches", tags=["matches"])
