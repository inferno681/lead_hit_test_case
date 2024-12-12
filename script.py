import asyncio

from httpx import AsyncClient

BASE_URL = 'http://127.0.0.1:8000/api/'

REQUEST_DATA = [
    {'Name': 'Ivan'},
    {
        'some_email': 'ivan@ivanov.ru',
        'phone': '+7 123 123 12 12',
        'check_date': '21.12.2024',
    },
    {'surname': 'Ivanov'},
]


async def get_form_params_requests(base_url: str) -> list[tuple]:
    """Выполнение запросов с данными в параметрах запроса."""
    result = []
    async with AsyncClient(base_url=base_url) as client:
        for data in REQUEST_DATA:
            response = await client.post('/get_form', params=data)
            result.append((data, response.status_code, response.json()))
    return result


async def get_form_body_requests(base_url: str) -> list[tuple]:
    """Выполнение запросов с данными в теле запроса."""
    result = []
    async with AsyncClient(base_url=base_url) as client:
        for data in REQUEST_DATA:
            response = await client.post('/get_form', json=data)
            result.append((data, response.status_code, response.json()))
    return result


async def main():
    """Выполнение запросов и вывод отчетов."""
    params_result = await get_form_params_requests(BASE_URL)
    body_result = await get_form_body_requests(BASE_URL)
    print('\n=== Params Requests ===')
    for request, status_code, response in params_result:
        print(
            f'Request: {request}\nStatus Code: {status_code}\n'
            f'Response: {response}\n{"-" * 40}',
        )

    print('\n=== Body Requests ===')
    for request, status_code, response in body_result:
        print(
            f'Request: {request}\nStatus Code: {status_code}\n'
            f'Response: {response}\n{"-" * 40}',
        )


if __name__ == '__main__':
    asyncio.run(main())
