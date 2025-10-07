from typing import Optional


def valid_date(date_string: str) -> bool:
    try:
        trimmed_input: str = date_string.strip()
        part_month, part_day, part_year = trimmed_input.split('-')

        numeric_month: int = int(part_month)
        numeric_day: int = int(part_day)
        numeric_year: int = int(part_year)

        if not (1 <= numeric_month <= 12):
            return False

        if numeric_month == 2:
            if not (1 <= numeric_day <= 29):
                return False
        elif numeric_month in {4, 6, 9, 11}:
            if not (1 <= numeric_day <= 30):
                return False
        else:
            if not (1 <= numeric_day <= 31):
                return False

    except Exception:
        return False

    return True