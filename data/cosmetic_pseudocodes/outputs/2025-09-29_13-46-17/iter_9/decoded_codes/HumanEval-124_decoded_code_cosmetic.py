from typing import Any


def valid_date(date_str: str) -> bool:
    try:
        components = date_str.split("-")
        if len(components) != 3:
            return False
        year_str, month_str, day_str = components
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)

        if not (1 <= month <= 12):
            return False

        if month in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= day <= 31):
                return False
        elif month in {4, 6, 9, 11}:
            if not (1 <= day <= 30):
                return False
        elif month == 2:
            if not (1 <= day <= 29):
                return False

        return True
    except Exception:
        return False