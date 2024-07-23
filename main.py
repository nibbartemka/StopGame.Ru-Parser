from parser import StopGameParser as sgp, ExcelSaver as xlsxsave
import datetime

excel_filename = 'example.xlsx'
datefrom = datetime.date(2024, 1, 22)
dateto = datetime.date(2024, 1, 23)


def main():
    parser = sgp.StopGameParser((datefrom, dateto))
    parser.parse()
    xlsxsave.ExcelSaver.to_excel(parser.parsed_pages, excel_filename)


if __name__ == '__main__':
    main()
