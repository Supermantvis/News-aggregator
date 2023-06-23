from datetime import datetime, date
import locale
import re

def date_formating(some_date):
    ru_months = {
        'Январь': 1,
        'Февраль': 2,
        'Март': 3,
        'Апрель': 4,
        'Май': 5,
        'Июнь': 6,
        'Июль': 7,
        'Август': 8,
        'Сентябрь': 9,
        'Октябрь': 10,
        'Ноябрь': 11,
        'Декабрь': 12
        }
    
    lt_months = {
        'sausio': 1,
        'vasario': 2,
        'kovo': 3,
        'balandžio': 4,
        'gegužės': 5,
        'birželio': 6,
        'liepos': 7,
        'rugpjūčio': 8,
        'rugsėjo': 9,
        'spalio': 10,
        'lapkričio': 11,
        'gruodžio': 12
        }
    
    pattern = r"(\d{4}) m\.\s+(\w+)\s+(\d+)"
    match = re.search(pattern, some_date)
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)
    if '\u0410' <= month <= '\u044F':
        formated_date = date(int(year), ru_months[month.capitalize()], int(day))
    elif month[0].isupper():
        date_object = datetime.strptime(f"{year} {month} {day}", "%Y %B %d")
        formated_date = date_object.strftime("%Y-%m-%d")
    else:
        formated_date = date(int(year), lt_months[month], int(day))
    return formated_date

dates = [
    "2023 m. май 12 d. 09:32",
    "2023 m. июнь 12 d. 18:31",
    "2023 m. март 19 d. 10:59",
    "2023 m. birželio 20 d. 14:43",
    "2023 m. июнь 08 d. 08:26",
    "2023 m. июнь 06 d. 23:43",
    "2023 m. апрель 29 d. 18:52",
    "2023 m. июнь 04 d. 20:44",
    "2023 m. June 04 d. 17:38",
    "2023 m. июнь 18 d. 23:18",
    "2023 m. июнь 19 d. 21:54",
    "2023 m. июнь 21 d. 09:52",
    "2023 m. май 22 d. 10:42",
    "2023 m. март 05 d. 18:48",
    "2023 m. май 12 d. 10:34",
    "2023 m. June 05 d. 10:32",
    "2023 m. март 19 d. 21:03",
    "2023 m. апрель 02 d. 11:26",
    "2023 m. май 07 d. 00:42",
    "2023 m. июнь 19 d. 23:29",
    "2023 m. июнь 09 d. 12:04",
    "2023 m. июнь 20 d. 10:14",
    "2023 m. июнь 13 d. 19:25",
    "2023 m. май 08 d. 00:49",
    "2023 m. апрель 29 d. 13:29",
    "2023 m. апрель 27 d. 10:46",
    "2023 m. июнь 21 d. 11:03",
    "2023 m. март 11 d. 17:38",
    "2023 m. июнь 18 d. 21:06",
    "2023 m. апрель 07 d. 14:12",
    "2023 m. June 07 d. 17:09",
    "2023 m. апрель 13 d. 13:31",
    "2023 m. июнь 09 d. 19:36",
    "2023 m. апрель 01 d. 11:54",
    "2023 m. июнь 19 d. 21:00",
    "2023 m. июнь 07 d. 08:00",
    "2023 m. июнь 21 d. 10:24",
    "2023 m. июнь 20 d. 22:50",
    "2023 m. май 25 d. 07:56",
    "2023 m. March 04 d. 18:46",
    "2023 m. июнь 02 d. 19:50"
]

for date_ in dates:
    print(date_formating(date_))