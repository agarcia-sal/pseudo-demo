from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        date_input = date_string.strip()
        parts = date_input.split("-")
        if len(parts) != 3:
            return False
        month_num = int(parts[0])
        day_num = int(parts[1])
        year_num = int(parts[2])

        if not (1 <= month_num <= 12):
            return False

        if month_num in {1, 3, 5, 7, 8, 10, 12}:
            if day_num < 1 or day_num > 31:
                return False
        elif month_num in {4, 6, 9, 11}:
            if day_num < 1 or day_num > 30:
                return False
        elif month_num == 2:
            if day_num < 1 or day_num > 29:
                return False
        else:
            # This else is unreachable due to the month range check above,
            # but is here for completeness
            return False
    except Exception:
        return False

    return True