from typing import Tuple


def valid_date(date_string: str) -> bool:
    try:
        date_string = date_string.strip()
        month_string, day_string, year_string = date_string.split('-')
        month, day, year = int(month_string), int(day_string), int(year_string)
        if not (1 <= month <= 12):
            return False
        if month in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= day <= 31):
                return False
        elif month in {4, 6, 9, 11}:
            if not (1 <= day <= 30):
                return False
        else:  # month == 2
            if not (1 <= day <= 29):
                return False
    except Exception:
        return False
    return True