from typing import TypeAlias, Dict, List, Union
import datetime

import pandas as pd

date: TypeAlias = datetime.date
parsedData: TypeAlias = List[Dict[str, Union[date, str]]]


class ExcelSaver(object):
    """Class for saving parsed data to excel"""
    EXCEL_EXTENSTION = '.xlsx'

    @classmethod
    def to_excel(cls, data: parsedData, filename: str) -> None:
        df = pd.DataFrame(data)
        if cls.EXCEL_EXTENSTION not in filename:
            filename = f'{filename}{cls.EXCEL_EXTENSTION}'

        df.to_excel(filename, index=False)
