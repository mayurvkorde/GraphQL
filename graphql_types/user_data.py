import strawberry
from crud.user_data import get_user_data, create_user_data
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

@strawberry.type
class User:
    name: str
    email: str
    address: str

    @staticmethod
    async def fetch_user_info(session: AsyncSession) -> "User":
        user_result = await get_user_data(session=session)
        data: List = []
        for result in user_result:
            user_data = User(name=result.name,
                             email=result.email,
                             address=result.address
                             )
            data.append(user_data)
        return data

    @staticmethod
    async def create_user_info(session: AsyncSession, user_input) -> "User":
        user_result = await create_user_data(session=session, user_input=user_input)
        data: List = []
        for result in user_result:
            user_data = User(name=result.name,
                             email=result.email,
                             address=result.address)
            data.append(user_data)
        return data