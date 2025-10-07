from typing import Union


def valid_date(date_string: str) -> bool:
    try:
        date_string = date_string.strip()
        month_str, day_str, year_str = date_string.split('-')
        month, day, year = int(month_str), int(day_str), int(year_str)

        if month < 1 or month > 12:
            return False

        if month in {1, 3, 5, 7, 8, 10, 12} and (day < 1 or day > 31):
            return False

        if month in {4, 6, 9, 11} and (day < 1 or day > 30):
            return False

        if month == 2 and (day < 1 or day > 29):
            return False

    except (ValueError, AttributeError):
        return False

    return True