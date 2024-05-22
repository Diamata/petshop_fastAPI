from src.repository.db_connection import async_session_maker
from sqlalchemy import select, insert, delete


class BaseRepo:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        pass

    @classmethod
    async def find_by_id(cls, model_id: int):
        pass

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        pass

    @classmethod
    async def delete_by_id(cls, model_id):
        pass

    @classmethod
    async def create_new(cls, **data):
        pass

    @classmethod
    async def update_by_id(cls, model_id):
        pass
