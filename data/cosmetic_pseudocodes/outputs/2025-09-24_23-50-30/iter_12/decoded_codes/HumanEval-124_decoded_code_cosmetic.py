from typing import Optional


def valid_date(date_string: str) -> bool:
    try:
        trimmed_input: str = date_string.strip()
        parts: list[str] = trimmed_input.split('-')
        if len(parts) != 3:
            return False
        first_part, second_part, third_part = parts
        num_month: int = int(first_part)
        num_day: int = int(second_part)
        num_year: int = int(third_part)

        if num_month <= 0 or num_month >= 13:
            return False

        if num_month in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= num_day <= 31):
                return False
        elif num_month in {4, 6, 9, 11}:
            if not (1 <= num_day <= 30):
                return False
        elif num_month == 2:
            if not (1 <= num_day <= 29):
                return False

    except (ValueError, IndexError):
        return False

    return True