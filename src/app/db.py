from motor.motor_asyncio import AsyncIOMotorClient

from config import config


class MongoDB:
    """Класс для операций с бд."""

    def __init__(
        self,
        client: AsyncIOMotorClient,
        db_name: str,
        collection_name: str,
    ):
        """Конструктор класса."""
        self.client = client
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    async def add_form(self, form: dict) -> None:
        """Создание записи в бд."""
        await self.collection.insert_one(form)

    async def get_form(self, fields: dict) -> dict | None:
        """Получение первого совпадения из бд."""
        return await self.collection.find_one(fields)

    async def get_form_list(self, fields: dict) -> list[dict]:
        """Получение списка всех совпадений из бд."""
        return [document async for document in self.collection.find(fields)]

    def close(self):
        """Закрытие клиента и соединений с бд."""
        self.client.close()


mongo = MongoDB(
    AsyncIOMotorClient(config.database_url),
    config.service.db_name,
    config.service.db_collection_name,
)


def get_mongo():
    """Функция получения класса для запросов в бд."""
    return mongo
