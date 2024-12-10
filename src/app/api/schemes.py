from pydantic import BaseModel, PrivateAttr, model_validator

from app.constants import VALIDATORS


class BaseForm(BaseModel):
    """Схема валидации данных."""

    _field_types: dict = PrivateAttr(default_factory=dict)

    class Config:
        """Настройки схемы для добавления атрибутов класса."""

        extra = 'allow'

    @model_validator(mode='after')
    def validate_fields(self):
        """Валидация всех полей с определением их типов."""
        form = self.model_dump()
        for field_name, value in form.items():
            if field_name == 'name':
                self._field_types[field_name] = value
            else:
                self._field_types[field_name] = self.get_field_type(value)
        return self

    @staticmethod
    def get_field_type(value: str) -> str:
        """Определяет тип поля на основе приоритетного порядка: email > телефон > дата > текст."""  # noqa: E501
        if isinstance(value, str):
            for field_type, validator in VALIDATORS.items():
                if validator.match(value):
                    return field_type
        return 'text'


class ReadForm(BaseModel):
    """Схема ответа с названием формы."""

    name: str


class CreateForm(ReadForm, BaseForm):
    """Схема создания формы."""

    class Config:
        """Настройки схемы для добавления атрибутов класса."""

        extra = 'allow'
