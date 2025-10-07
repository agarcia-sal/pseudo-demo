from typing import Union


def valid_date(date: str) -> bool:
    try:
        date_stripped = date.strip()
        month_str, day_str, year_str = date_stripped.split('-')
        month = int(month_str)
        day = int(day_str)
        # Year is parsed but not validated beyond int conversion, per the pseudocode
        year = int(year_str)

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
            # This else is logically unreachable because of the first month range check
            return False
    except Exception:
        return False
    return True