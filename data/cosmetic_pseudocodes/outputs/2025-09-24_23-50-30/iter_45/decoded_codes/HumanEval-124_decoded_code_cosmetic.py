from typing import Optional


def valid_date(date_string: str) -> bool:
    try:
        trimmed_string: str = date_string.strip()
        parts: list[str] = trimmed_string.split('-')
        if len(parts) != 3:
            return False

        part_one: str = parts[0]
        part_two: str = parts[1]
        part_three: str = parts[2]

        num_month: int = int(part_one)
        num_day: int = int(part_two)
        num_year: int = int(part_three)

        if num_month < 1 or num_month > 12:
            return False
        if num_month in {1, 3, 5, 7, 8, 10, 12} and (num_day < 1 or num_day > 31):
            return False
        if num_month in {4, 6, 9, 11} and (num_day < 1 or num_day > 30):
            return False
        if num_month == 2 and (num_day < 1 or num_day > 29):
            return False

    except (ValueError, IndexError):
        return False

    return True