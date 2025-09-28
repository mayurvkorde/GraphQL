from sqlalchemy import select, insert
from models.user_model import User
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user_data import UserDataInput

async def get_user_data(session: AsyncSession) -> List[User]:
    query = select(User)
    result = await session.execute(query)
    return result.scalars().all()

async def create_user_data(session: AsyncSession, user_input: UserDataInput) -> List[User]:
    query = insert(User).values(user_input.__dict__)
    await session.execute(query)
    await  session.commit()
    return [user_input]