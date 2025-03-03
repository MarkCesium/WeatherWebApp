import logging
from typing import TYPE_CHECKING

from sqlalchemy import select

from src.core.models import Query

from .schemas import QueryCreate, QueryRead

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

async def query_write(session: "AsyncSession", query: QueryCreate) -> None:
    session.add(
        Query(**(query.model_dump()))
    )
    await session.commit()

async def queries_read(session: "AsyncSession") -> list[QueryRead]:
    result = await session.scalars(select(Query))
    queries = result.all()
    
    return [QueryRead.model_validate(q) for q in queries]