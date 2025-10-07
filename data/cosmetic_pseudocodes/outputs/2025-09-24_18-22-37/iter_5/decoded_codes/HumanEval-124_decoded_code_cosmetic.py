from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed_str = date_string.strip()
        parts = trimmed_str.split('-')
        str_mon = parts[0]
        str_day = parts[1]
        str_yr = parts[2]

        int_mon = int(str_mon)
        int_day = int(str_day)
        int_yr = int(str_yr)

        if int_mon < 1 or int_mon > 12:
            return False

        if int_mon == 2:
            if int_day < 1 or int_day > 29:
                return False
        elif int_mon in {4, 6, 9, 11}:
            if int_day < 1 or int_day > 30:
                return False
        elif int_mon in {1, 3, 5, 7, 8, 10, 12}:
            if int_day < 1 or int_day > 31:
                return False

    except (IndexError, ValueError):
        return False

    return True