import asyncio

import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient


@pytest.fixture(scope='session')
def event_loop():
    """Управление циклом событий для асинхронных тестов."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def forms_data():
    """Данные для бд."""
    return (
        {
            'name': 'Contact form',
            'Name': 'text',
            'surname': 'text',
            'phone number': 'phone',
            'email': 'email',
        },
        {
            'name': 'Feedback Form',
            'Name': 'text',
            'surname': 'text',
            'email': 'email',
            'message': 'text',
            'rating': 'text',
        },
        {
            'name': 'Registration Form',
            'username': 'text',
            'password': 'text',
            'confirm_password': 'text',
            'email': 'email',
            'phone_number': 'phone',
        },
        {
            'name': 'Hotel Booking Form',
            'first_name': 'text',
            'last_name': 'text',
            'email': 'email',
            'phone_number': 'phone',
            'check_in_date': 'date',
            'check_out_date': 'date',
            'number_of_guests': 'text',
            'room_type': 'text',
        },
        {
            'name': 'Job Application Form',
            'full_name': 'text',
            'email': 'email',
            'phone_number': 'phone',
            'position_applied': 'text',
            'resume_link': 'text',
            'cover_letter': 'text',
            'available_start_date': 'date',
        },
    )


@pytest_asyncio.fixture(scope='session')
async def client():
    """Клиент для тестирования."""
    from app.main import app

    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url='http://127.0.0.1:8000/api/',
        ) as client:
            yield client
