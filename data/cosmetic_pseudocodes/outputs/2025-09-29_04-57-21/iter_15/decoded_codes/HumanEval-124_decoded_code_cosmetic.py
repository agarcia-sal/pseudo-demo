from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed_str = date_string.strip()
        parts = trimmed_str.split('-')
        if len(parts) != 3:
            return False

        month_part, day_part, year_part = parts
        month_val = int(month_part)
        day_val = int(day_part)
        year_val = int(year_part)  # year_val is not used further, but parsing ensures numeric

        if not (1 <= month_val <= 12):
            return False

        if month_val == 2:
            if not (1 <= day_val <= 29):
                return False
        elif month_val in {4, 6, 9, 11}:
            if not (1 <= day_val <= 30):
                return False
        else:
            if not (1 <= day_val <= 31):
                return False

    except Exception:
        return False

    return True