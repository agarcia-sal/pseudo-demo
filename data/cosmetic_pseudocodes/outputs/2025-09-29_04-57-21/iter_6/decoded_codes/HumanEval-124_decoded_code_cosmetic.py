from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed: str = date_string.strip()
        parts: list[str] = trimmed.split('-')
        mon_str, dy_str, yr_str = parts  # expecting exactly 3 parts

        mon_val: int = int(mon_str)
        dy_val: int = int(dy_str)
        yr_val: int = int(yr_str)

        if not (1 <= mon_val <= 12):
            return False

        if mon_val in {1, 3, 5, 7, 8, 10, 12}:
            if dy_val < 1 or dy_val > 31:
                return False
        elif mon_val in {4, 6, 9, 11}:
            if dy_val < 1 or dy_val > 30:
                return False
        elif mon_val == 2:
            if dy_val < 1 or dy_val > 29:
                return False

    except Exception:  # catch all errors from split or int conversions etc.
        return False

    return True