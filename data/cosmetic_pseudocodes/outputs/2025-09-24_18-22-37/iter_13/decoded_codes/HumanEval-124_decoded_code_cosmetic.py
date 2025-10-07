from typing import Optional


def valid_date(input_string: str) -> bool:
    is_error_occurred: bool = False
    try:
        stripped_string: str = input_string.strip()
        parts: list[str] = stripped_string.split('-')
        mon_str: str = parts[0]
        dy_str: str = parts[1]
        yr_str: str = parts[2]

        mon_val: int = int(mon_str)
        dy_val: int = int(dy_str)
        yr_val: int = int(yr_str)
    except Exception:
        is_error_occurred = True

    if is_error_occurred:
        return False

    is_month_valid: bool = 1 <= mon_val <= 0xC  # 12 in hex
    if not is_month_valid:
        return False

    if mon_val in {1, 3, 5, 7, 8, 10, 12}:
        is_day_valid: bool = 1 <= dy_val <= 31
        if not is_day_valid:
            return False
    elif mon_val in {4, 6, 9, 11}:
        is_day_valid = 1 <= dy_val <= 30
        if not is_day_valid:
            return False
    elif mon_val == 2:
        is_day_valid = 1 <= dy_val <= 0x1D  # 29 decimal
        if not is_day_valid:
            return False

    return True