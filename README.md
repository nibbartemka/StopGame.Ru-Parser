# Парсер новостей с сайта StopGame.ru
### Данный проект позволяет пользователю получить новости с сайта stopgame.ru в рамках указанного диапазона дат, а также сохранить результаты в Excel-файл.
Были использованы следующие библиотеки: `pandas`, `BeautifulSoup4`, `requests`, `concurent` 
<br/><br/>
### Установка и настройка
1. Сформируйте и активируйте виртуальное окружение:
```bash
python -m venv .venv
source ./.venv/Scripts/activate
```
2. Установите необходимые библиотеки:
```bash
pip install -r requirements.txt
```
3. Запустите файл `main.py`:
```bash
python main.py
```
<br/><br/>
### Структура репозитория
```bash
StopGameRuParser/
├── parser/
│   ├── __init.py__
│   ├── subpackages/
│   |   ├── NewsCardExtractor.py
│   |   └── ExcelSaver.py
|   ├── StopGameParser.py
│   └── ExcelSaver.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```