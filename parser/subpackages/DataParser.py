import re
import datetime
from typing import TypeAlias

date: TypeAlias = datetime.date


class DataParser(object):
    """Class for processing dates from news."""
    DATE_FORMAT = '%d %m %Y'

    MONTH_NUM = {
      'января': '01',
      'февраля': '02',
      'марта': '03',
      'апреля': '04',
      'мая': '05',
      'июня': '06',
      'июля': '07',
      'августа': '08',
      'сентября': '09',
      'октября': '10',
      'ноября': '11',
      'декабря': '12',
    }

    @classmethod
    def process_date(cls, date_value: str) -> date:
        if 'сегодня' in date_value.lower():
            return datetime.date.today()
        if 'вчера' in date_value.lower():
            return datetime.date.today() - datetime.timedelta(days=1)

        if re.match(r'\d{1,2}\s[а-я]+', date_value, flags=re.IGNORECASE):
            current_year = datetime.datetime.now().year
            date_value = f'{date_value} {current_year}'

        date_parts = date_value.split()
        date_parts[1] = cls.MONTH_NUM[date_parts[1]]
        date_value_by_format = ' '.join(date_parts)

        return datetime.datetime.strptime(date_value_by_format,
                                          cls.DATE_FORMAT).date()
