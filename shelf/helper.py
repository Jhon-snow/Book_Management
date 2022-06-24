# date_string = '12-25-2018'
import datetime

from shelf.Excpetions import InvalidDateException


format = "%d-%m-%Y"

def validate_date(user_date):
    """Validate the given Date"""
    try:
        return bool(datetime.datetime.strptime(user_date, format))
    except ValueError:
        return False
    

