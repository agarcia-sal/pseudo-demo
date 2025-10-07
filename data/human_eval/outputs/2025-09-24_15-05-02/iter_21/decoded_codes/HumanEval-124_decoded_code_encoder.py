from typing import Optional

def valid_date(date_string: str) -> bool:
    try:
        date_string = date_string.strip()
        month_string, day_string, year_string = date_string.split('-')
        month: int = int(month_string)
        day: int = int(day_string)
        year: int = int(year_string)

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
            # This else is technically unreachable because month bounds checked above,
            # but kept for completeness.
            return False

    except Exception:
        return False

    return True