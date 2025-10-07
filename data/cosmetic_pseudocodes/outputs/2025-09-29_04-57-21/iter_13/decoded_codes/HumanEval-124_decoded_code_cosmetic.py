from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed_input: str = date_string.strip()
        parts: list[str] = trimmed_input.split('-')
        mon_str: str = parts[0]
        d_str: str = parts[1]
        yr_str: str = parts[2]
        m: int = int(mon_str)
        d: int = int(d_str)
        y: int = int(yr_str)

        if not (1 <= m <= 12):
            return False

        if m in {1, 3, 5, 7, 8, 10, 12}:
            if d < 1 or d > 31:
                return False
        elif m in {4, 6, 9, 11}:
            if d < 1 or d > 30:
                return False
        else:
            # m == 2 here
            if d < 1 or d > 29:
                return False

    except (IndexError, ValueError):
        return False

    return True