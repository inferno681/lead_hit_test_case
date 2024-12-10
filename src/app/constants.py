import re

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
