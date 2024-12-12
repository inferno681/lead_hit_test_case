import re

from pymongo import UpdateOne

"""Регулярные выражения и валидаторы."""
EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
PHONE_REGEX = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
DATE_REGEX = re.compile(
    r'^(19|20)\d\d-(0[1-9]|1[012])-(0[1-9]|[12]\d|3[01])$|'
    r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.(19|20)\d\d$',
)

VALIDATORS: dict[str, re.Pattern] = {
    'email': EMAIL_REGEX,
    'phone': PHONE_REGEX,
    'date': DATE_REGEX,
}

"""Сообщения об ошибках."""
FORM_EXISTS_MESSAGE = 'Форма с названием {name} уже есть в базе данных.'
NO_DATA_MESSAGE = 'Данные не предоставлены'

"""Данные для заполнения бд."""
DB_DATA = [
    UpdateOne(
        {'name': 'Contact form'},  # Фильтр
        {
            '$set': {
                'Name': 'text',
                'surname': 'text',
                'phone number': 'phone',
                'email': 'email',
            },
        },
        upsert=True,  # Если записи нет, создаем новую
    ),
    UpdateOne(
        {'name': 'Feedback Form'},
        {
            '$set': {
                'Name': 'text',
                'surname': 'text',
                'email': 'email',
                'message': 'text',
                'rating': 'text',
            },
        },
        upsert=True,
    ),
    UpdateOne(
        {'name': 'Registration Form'},
        {
            '$set': {
                'username': 'text',
                'password': 'text',
                'confirm_password': 'text',
                'email': 'email',
                'phone_number': 'phone',
            },
        },
        upsert=True,
    ),
    UpdateOne(
        {'name': 'Hotel Booking Form'},
        {
            '$set': {
                'first_name': 'text',
                'last_name': 'text',
                'email': 'email',
                'phone_number': 'phone',
                'check_in_date': 'date',
                'check_out_date': 'date',
                'number_of_guests': 'text',
                'room_type': 'text',
            },
        },
        upsert=True,
    ),
    UpdateOne(
        {'name': 'Job Application Form'},
        {
            '$set': {
                'full_name': 'text',
                'email': 'email',
                'phone_number': 'phone',
                'position_applied': 'text',
                'resume_link': 'text',
                'cover_letter': 'text',
                'available_start_date': 'date',
            },
        },
        upsert=True,
    ),
]
