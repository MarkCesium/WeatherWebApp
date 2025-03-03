from fastapi import APIRouter, HTTPException, status

from .service import get_weather
from .schemas import WeatherResponse

router = APIRouter(prefix="/weather")


@router.get("/", response_model=WeatherResponse)
async def weather_get(city: str) -> WeatherResponse | None:
    broadcast = await get_weather(city)
    
    if isinstance(broadcast, WeatherResponse):
        return broadcast

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="City not found",
    )
    