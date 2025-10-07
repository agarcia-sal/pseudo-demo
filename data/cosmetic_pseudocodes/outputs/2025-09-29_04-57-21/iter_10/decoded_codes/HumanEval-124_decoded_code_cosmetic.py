from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed_string = date_string.strip()
        part_array = trimmed_string.split('-')
        if len(part_array) != 3:
            return False
        part1, part2, part3 = part_array

        num_month = int(part1)
        num_day = int(part2)
        num_year = int(part3)

        if not (1 <= num_month <= 12):
            return False

        if num_month == 2:
            if num_day < 1 or num_day > 29:
                return False
        elif num_month in {4, 6, 9, 11}:
            if num_day < 1 or num_day > 30:
                return False
        else:
            if num_day < 1 or num_day > 31:
                return False

    except Exception:
        return False

    return True