from typing import Any


def valid_date(string_input: str) -> bool:
    try:
        trimmed_string: str = string_input.strip()
        parts_list: list[str] = trimmed_string.split('-')
        if len(parts_list) != 3:
            return False
        part_one, part_two, part_three = parts_list

        num_month: int = int(part_one)
        num_day: int = int(part_two)
        num_year: int = int(part_three)

        if not (1 <= num_month <= 12):
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
        else:
            # This case is logically unreachable due to previous checks but kept for clarity
            return False

    except Exception:
        return False

    return True