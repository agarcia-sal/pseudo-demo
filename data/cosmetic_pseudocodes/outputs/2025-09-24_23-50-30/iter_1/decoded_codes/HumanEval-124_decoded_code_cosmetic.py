from typing import List

def valid_date(date_string: str) -> bool:
    try:
        trimmed: str = date_string.strip()
        parts: List[str] = trimmed.split('-')
        month: int = int(parts[0])
        day: int = int(parts[1])
        year: int = int(parts[2])

        if not (1 <= month <= 12):
            return False

        if month == 2:
            valid_days = range(1, 30)  # up to 29
        elif month in {4, 6, 9, 11}:
            valid_days = range(1, 31)  # up to 30
        else:
            valid_days = range(1, 32)  # up to 31

        if day not in valid_days:
            return False

    except Exception:
        return False

    return True