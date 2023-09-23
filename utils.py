from datetime import datetime, date
import locale
    

def datetime_to_dateformat(input_date: datetime, format: str):
    locale.setlocale(locale.LC_TIME, "es_ES")
    return input_date.strftime(format)
