from typing import TYPE_CHECKING, Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.core.db_helper import db_helper

from .dao import queries_read, query_write
from .schemas import QueryCreate, QueryRead
from .service import get_weather

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/weather")


@router.get("/", response_model=QueryCreate)
async def weather_get(city: str, session: Annotated["AsyncSession", Depends(db_helper.async_session_dependency)]) -> QueryCreate | None:
    broadcast = await get_weather(city)
    
    if not isinstance(broadcast, QueryCreate):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="City not found",
        )
    
    await query_write(session=session, query=broadcast)
    
    return broadcast

@router.get("/history", response_model=list[QueryRead])
async def queries_get(session: Annotated["AsyncSession", Depends(db_helper.async_session_dependency)]) -> list[QueryRead]:
    return await queries_read(session=session)
    
    