from fastapi import APIRouter

from .weather.views import router as weather_router

api_router = APIRouter(prefix="/api")
api_router.include_router(weather_router)

__all__ = ("api_router",)