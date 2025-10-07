from typing import Tuple

def valid_date(date_string: str) -> bool:
    try:
        month_str, day_str, year_str = date_string.strip().split('-')
        month, day, year = int(month_str), int(day_str), int(year_str)

        if month < 1 or month > 12:
            return False
        if month in {1, 3, 5, 7, 8, 10, 12} and not (1 <= day <= 31):
            return False
        if month in {4, 6, 9, 11} and not (1 <= day <= 30):
            return False
        if month == 2 and not (1 <= day <= 29):
            return False

    except Exception:
        return False

    return True