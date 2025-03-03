from datetime import datetime

from pydantic import BaseModel


class QueryRead(BaseModel):
    id: int
    city: str
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float
    description: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class QueryCreate(BaseModel):
    city: str
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float
    description: str
