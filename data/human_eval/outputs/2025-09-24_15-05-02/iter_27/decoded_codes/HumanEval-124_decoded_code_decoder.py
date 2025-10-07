from typing import Optional


def valid_date(date: str) -> bool:
    try:
        trimmed_date: str = date.strip()
        month_str, day_str, year_str = trimmed_date.split('-')
        month: int = int(month_str)
        day: int = int(day_str)
        year: int = int(year_str)

        if month < 1 or month > 12:
            return False

        if month in {1, 3, 5, 7, 8, 10, 12}:
            if day < 1 or day > 31:
                return False
        elif month in {4, 6, 9, 11}:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if day < 1 or day > 29:
                return False
        else:
            return False

    except (ValueError, AttributeError):
        return False

    return True