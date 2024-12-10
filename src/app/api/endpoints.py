from fastapi import APIRouter, Request

from app.api import BaseForm, CreateForm
from config import config

router = APIRouter(tags=[config.service.tags_metadata['name']])


@router.post('/add_form', response_model=CreateForm)
async def add_form(
    request: Request,
    form: CreateForm | None = None,
    query: str | None = None,
):
    """Эндпоинт для добавления формы в базу данных."""
    return await request.app.state.form_service.add_form(query, form)


@router.post('/get_form')
async def get_form(
    request: Request,
    form: BaseForm | None = None,
    query: str | None = None,
):
    """Эндпоинт для получения формы из базы данных."""
    return await request.app.state.form_service.get_form(query, form)


@router.post('/get_form_list')
async def get_form_list(
    request: Request,
    form: BaseForm | None = None,
    query: str | None = None,
):
    """Эндпоинт для получения списка форм из базы данных."""
    return await request.app.state.form_service.get_form_list(query, form)
