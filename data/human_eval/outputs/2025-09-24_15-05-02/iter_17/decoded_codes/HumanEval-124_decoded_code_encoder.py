from typing import Any

def valid_date(date: Any) -> bool:
    try:
        trimmed_date: str = date.strip()  # type: ignore
        parts = trimmed_date.split('-')
        if len(parts) != 3:
            return False
        month_str, day_str, year_str = parts
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)
        if month < 1 or month > 12:
            return False
        if month in {1, 3, 5, 7, 8, 10, 12} and (day < 1 or day > 31):
            return False
        if month in {4, 6, 9, 11} and (day < 1 or day > 30):
            return False
        if month == 2 and (day < 1 or day > 29):
            return False
    except Exception:
        return False
    return True