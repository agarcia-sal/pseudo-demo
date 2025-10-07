from typing import Any


def valid_date(alphabetic: str) -> bool:
    try:
        trimmed_string: str = alphabetic.strip()
        split_array = trimmed_string.split('-')
        if len(split_array) != 3:
            return False

        month_val: int = int(split_array[0])
        day_val: int = int(split_array[1])
        year_val: int = int(split_array[2])

        if not (1 <= month_val <= 12):
            return False

        if month_val in {1, 3, 5, 7, 8, 10, 12}:
            max_days = 31
        elif month_val in {4, 6, 9, 11}:
            max_days = 30
        elif month_val == 2:
            max_days = 29
        else:
            # Defensive default in case of unexpected month_val (though already checked)
            return False

        if not (1 <= day_val <= max_days):
            return False

        return True
    except Exception:
        return False