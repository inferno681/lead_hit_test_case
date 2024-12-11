from fastapi import HTTPException, status

from app.api import BaseForm, CreateForm, ReadForm
from app.db import MongoDB


class FormService:
    """Сервис создания и получения форм."""

    def __init__(
        self,
        mongo: MongoDB,
    ):
        """Конструктор класса."""
        self.mongo = mongo

    def data_preparation(
        self,
        query: str | None,
        form: BaseForm | None,
    ) -> dict:
        """Проверка и подготовка данных."""
        if not (query or form):
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail='Данные не предоставлены',
            )
        if query:
            return BaseForm(**query)._field_types
        return form._field_types  # type: ignore

    async def add_form(self, query: str | None, form: CreateForm | None):
        """Запись новой формы."""
        data = self.data_preparation(query, form)
        await self.mongo.add_form(data)
        data.pop('_id')
        return data

    async def get_form(self, query: str | None, form: BaseForm | None):
        """Получение формы."""
        data = self.data_preparation(query, form)
        result = await self.mongo.get_form(data)
        if not result:
            return BaseForm(**data)
        return ReadForm(**result)

    async def get_form_list(self, query: str | None, form: BaseForm | None):
        """Получение списка форм."""
        data = self.data_preparation(query, form)
        result = await self.mongo.get_form_list(data)
        if not result:
            return BaseForm(**data)  # type: ignore
        return [ReadForm(**form) for form in result]
