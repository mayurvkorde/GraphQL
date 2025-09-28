from fastapi import FastAPI
import strawberry
from graphql_types.user_data import User
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from config.settings import AsyncSessionLocal
from strawberry.types import Info


@strawberry.type
class Query:
    @strawberry.field
    async def fetch_user_data(self, info: strawberry.types.Info) -> List[User]:
        session: AsyncSession = info.context["session"]
        return await User.fetch_user_info(session=session)