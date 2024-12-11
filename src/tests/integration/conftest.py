import pytest


@pytest.fixture()
def add_form_link():
    """Ссылка для загрузки форм."""
    return '/add_form'


@pytest.fixture()
def get_form_link():
    """Ссылка для получения форм."""
    return '/get_form'


@pytest.fixture()
def get_form_list_link():
    """Ссылка для получения списка форм."""
    return '/get_form_list'


@pytest.fixture()
def add_test_data():
    """Данные для теста загрузки формы."""
    return {
        'name': 'Some name',
        'text_field': 'Some text',
        'email_field': 'ivan@ivanov.ru',
        'phone_number': '+7 123 123 12 12',
        'date_1': '21.12.2024',
        'date_2': '2024-12-23',
        'int_field': 2,
    }


@pytest.fixture()
def test_response():
    """Данные для сравнения результата создания формы."""
    return {
        'name': 'Some name',
        'text_field': 'text',
        'email_field': 'email',
        'phone_number': 'phone',
        'date_1': 'date',
        'date_2': 'date',
        'int_field': 'text',
    }


@pytest.fixture(
    params=(
        {
            'data': {
                'surname': 'Ivanov',
                'phone number': '+7 123 123 12 12',
            },
            'response': {'name': 'Contact form'},
        },
        {
            'data': {
                'email': 'ivan@ivanov.ru',
                'message': 'Отличный сервис',
            },
            'response': {'name': 'Feedback Form'},
        },
        {
            'data': {
                'email': 'ivan@ivanov.ru',
                'phone_number': '+7 123 123 12 12',
                'check_in_date': '21.12.2024',
            },
            'response': {'name': 'Hotel Booking Form'},
        },
        {
            'data': {
                'some_email': 'ivan@ivanov.ru',
                'phone': '+7 123 123 12 12',
                'check_date': '21.12.2024',
            },
            'response': {
                'some_email': 'email',
                'phone': 'phone',
                'check_date': 'date',
            },
        },
    ),
    ids=(
        'Contact form',
        'Feedback Form',
        'Hotel Booking Form',
        'no form in db logic',
    ),
)
def get_test_data(request):
    """Данные для теста получения форм."""
    return request.param


@pytest.fixture(
    params=(
        {
            'data': {'Name': 'Ivan'},
            'response': [{'name': 'Contact form'}, {'name': 'Feedback Form'}],
        },
        {
            'data': {
                'some_email': 'ivan@ivanov.ru',
                'phone': '+7 123 123 12 12',
                'check_date': '21.12.2024',
            },
            'response': {
                'some_email': 'email',
                'phone': 'phone',
                'check_date': 'date',
            },
        },
    ),
    ids=('forms in db', 'no form in db logic'),
)
def get_form_list_data(request):
    """Данные для теста получения списка форм."""
    return request.param


@pytest.fixture()
def links(request, add_form_link, get_form_link, get_form_list_link):
    """Ссылки для тестирования."""
    if request.param == 'add_form_link':
        return add_form_link
    elif request.param == 'get_form_link)':
        return get_form_link
    elif request.param == 'get_form_list_link)':
        return get_form_list_link
