from urllib.parse import parse_qs

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

    def parse_query_to_form(
        self,
        query: str,
    ) -> dict:
        """Преобразование строки запроса в объект формы."""
        return {key: value[0] for key, value in parse_qs(query).items()}

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
            return self.parse_query_to_form(query)
        return form._field_types  # type: ignore

    async def add_form(self, query: str | None, form: CreateForm | None):
        """Запись новой формы."""
        data = self.data_preparation(query, form)
        await self.mongo.add_form(data)
        data.pop('_id')
        return data

    async def get_form(self, query: str | None, form: BaseForm | None):
        """Получение формы."""
        result = await self.mongo.get_form(self.data_preparation(query, form))
        if not result:
            return BaseForm(**form._field_types)  # type: ignore

        return ReadForm(**result)

    async def get_form_list(self, query: str | None, form: BaseForm | None):
        """Получение списка форм."""
        result = await self.mongo.get_form_list(
            self.data_preparation(query, form),
        )
        if not result:
            return BaseForm(**form._field_types)  # type: ignore

        return [ReadForm(**form) for form in result]
