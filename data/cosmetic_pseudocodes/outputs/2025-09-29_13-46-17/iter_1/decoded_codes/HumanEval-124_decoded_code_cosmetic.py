from typing import Optional


def valid_date(date_string: str) -> bool:
    try:
        trimmed_date = date_string.strip()
        parts = trimmed_date.split('-')
        if len(parts) != 3:
            return False

        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

        if month < 1 or month > 12:
            return False

        if month == 2:
            if day < 1 or day > 29:
                return False
        elif month in (4, 6, 9, 11):
            if day < 1 or day > 30:
                return False
        else:
            if day < 1 or day > 31:
                return False

    except Exception:
        return False

    return True