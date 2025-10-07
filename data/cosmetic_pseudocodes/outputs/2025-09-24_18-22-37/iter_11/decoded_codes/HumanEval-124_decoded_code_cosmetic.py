from typing import Any


def valid_date(date_string_param: str) -> bool:
    try:
        trimmed_string: str = date_string_param.strip()
        parts_array: list[str] = trimmed_string.split('-')

        part_index: int = 0
        month_num: int = int(parts_array[part_index])
        part_index += 1
        day_num: int = int(parts_array[part_index])
        part_index += 1
        year_num: int = int(parts_array[part_index])

        if month_num < 1 or month_num > 12:
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
            return False

        return True

    except (ValueError, IndexError):
        return False