from fastapi import FastAPI
import strawberry
from graphql_types.user_data import User
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from config.settings import AsyncSessionLocal
from strawberry.types import Info
from schemas.user_data import UserDataInput


@strawberry.type
class Mutation:
    @strawberry.field
    async def create_user_data(self, user_input: UserDataInput, info: strawberry.types.Info) -> List[User]:
        session: AsyncSession = info.context["session"]
        return await User.create_user_info(session=session, user_input=user_input)