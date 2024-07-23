import re
import datetime
from typing import TypeAlias

from .settings import DATE_FORMAT, MONTH_NUM

date: TypeAlias = datetime.date


class DataParser(object):
    """Class for processing dates from news."""

    @staticmethod
    def process_date(date_value: str) -> date:
        if 'сегодня' in date_value.lower():
            return datetime.date.today()
        if 'вчера' in date_value.lower():
            return datetime.date.today() - datetime.timedelta(days=1)

        if re.match(r'\d{1,2}\s[а-я]+', date_value, flags=re.IGNORECASE):
            current_year = datetime.datetime.now().year
            date_value = f'{date_value} {current_year}'

        date_parts = date_value.split()
        date_parts[1] = MONTH_NUM[date_parts[1]]
        date_value_by_format = ' '.join(date_parts)

        return datetime.datetime.strptime(date_value_by_format,
                                          DATE_FORMAT).date()
