from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed_string: str = date_string.strip()
        part_one, part_two, part_three = trimmed_string.split('-')

        month_num: int = int(part_one)
        day_num: int = int(part_two)
        year_num: int = int(part_three)

        if not (1 <= month_num <= 12):
            return False

        if month_num in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= day_num <= 31):
                return False

        elif month_num in {4, 6, 9, 11}:
            if not (1 <= day_num <= 30):
                return False

        else:  # month_num == 2
            if not (1 <= day_num <= 29):
                return False

    except Exception:
        return False

    return True