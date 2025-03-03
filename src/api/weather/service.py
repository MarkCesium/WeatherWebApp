import aiohttp

from src.core.config import settings
from .schemas import WeatherResponse

async def get_weather(city: str) -> WeatherResponse | None:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "appid": settings.api_keys.openweathermap,
                "units": "metric",
            }
        ) as resp:
            if resp.status != 200:
                return None
            data = await resp.json()
    return WeatherResponse(
        city=city,
        temperature=data["main"]["temp"],
        feels_like=data["main"]["feels_like"],
        humidity=data["main"]["humidity"],
        wind_speed=data["wind"]["speed"],
        description=data["weather"][0]["description"],
    )