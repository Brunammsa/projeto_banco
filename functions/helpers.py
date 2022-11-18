from datetime import date
from datetime import datetime


def date_to_str(date: date) -> str:
    return date.strftime('%d/%m/%Y')


def str_to_date(date: str) -> date:
    return datetime.strptime(date, '%d/%m/%Y')


def format_float_to_str_currency(value: float) -> str:
    return f'R$ {value:,.2f}'
