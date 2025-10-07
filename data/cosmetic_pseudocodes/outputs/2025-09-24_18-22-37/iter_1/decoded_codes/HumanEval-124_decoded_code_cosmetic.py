from typing import Union

def valid_date(date_string: str) -> bool:
    try:
        trimmed_date: str = date_string.strip()
        parts: list[str] = trimmed_date.split('-')
        if len(parts) != 3:
            return False
        month_num: int = int(parts[0])
        day_num: int = int(parts[1])
        year_num: int = int(parts[2])

        if month_num < 1 or month_num > 12:
            return False

        if month_num == 2:
            if day_num < 1 or day_num > 29:
                return False
        elif month_num in {4, 6, 9, 11}:
            if day_num < 1 or day_num > 30:
                return False
        else:
            if day_num < 1 or day_num > 31:
                return False

    except Exception:
        return False

    return True