from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed_date: str = date_string.strip()
        parts: list[str] = trimmed_date.split('-')
        mon_str, dy_str, yr_str = parts
        mon: int = int(mon_str)
        dy: int = int(dy_str)
        yr: int = int(yr_str)

        if not (1 <= mon <= 12):
            return False

        if mon in {1, 3, 5, 7, 8, 10, 12}:
            if dy < 1 or dy > 31:
                return False
        elif mon in {4, 6, 9, 11}:
            if dy < 1 or dy > 30:
                return False
        elif mon == 2:
            if dy < 1 or dy > 29:
                return False
        else:
            return False  # This covers any unforeseen month values

    except (ValueError, IndexError):
        return False

    return True