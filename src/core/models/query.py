from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Query(Base):
    __tablename__ = "queries"
    
    city: Mapped[str]
    temperature: Mapped[float]
    feels_like: Mapped[float]
    humidity: Mapped[int]
    wind_speed: Mapped[float]
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(True), default=lambda: datetime.now(timezone.utc))
    