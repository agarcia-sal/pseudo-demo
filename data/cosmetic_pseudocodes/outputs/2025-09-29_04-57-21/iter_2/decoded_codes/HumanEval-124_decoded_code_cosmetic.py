from typing import Any

def valid_date(date_string: str) -> bool:
    try:
        trimmed_input: str = date_string.strip()
        parts_list: list[str] = trimmed_input.split('-')
        mon_str, dy_str, yr_str = parts_list  # type: str, str, str

        mon_val: int = int(mon_str)
        dy_val: int = int(dy_str)
        yr_val: int = int(yr_str)

        if not (1 <= mon_val <= 12):
            return False

        if mon_val == 2:
            if dy_val < 1 or dy_val > 29:
                return False
        elif mon_val in {4, 6, 9, 11}:
            if dy_val < 1 or dy_val > 30:
                return False
        else:
            if dy_val < 1 or dy_val > 31:
                return False

    except (ValueError, IndexError):
        return False

    return True