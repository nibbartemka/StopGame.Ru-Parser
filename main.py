from parser import StopGameParser as sgp, ExcelSaver as xlsx_save
import datetime

full_path = "C:\\Users\\slend\\OneDrive\\Рабочий стол\\StopGameRuParser\\static\\{}"

date_from = datetime.date(2024, 1, 22)
date_to = datetime.date(2024, 1, 23)


def main():
    parser = sgp.StopGameParser((date_from, date_to))
    parser.parse()
    xlsx_save.ExcelSaver.to_excel(parser.parsed_pages,
                                  full_path.format('example.xlsx'))


if __name__ == '__main__':
    main()
