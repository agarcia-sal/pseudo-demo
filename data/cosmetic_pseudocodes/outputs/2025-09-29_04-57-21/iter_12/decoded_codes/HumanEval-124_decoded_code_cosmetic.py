from typing import Optional

def valid_date(date_string: str) -> bool:
    try:
        trimmed_input: str = date_string.strip()
        parts: list[str] = trimmed_input.split('-')
        if len(parts) != 3:
            return False

        mon_str, d_str, yr_str = parts

        mon_val: int = int(mon_str)
        d_val: int = int(d_str)
        yr_val: int = int(yr_str)

        if not (1 <= mon_val <= 12):
            return False

        if mon_val in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= d_val <= 31):
                return False
        elif mon_val in {4, 6, 9, 11}:
            if not (1 <= d_val <= 30):
                return False
        elif mon_val == 2:
            if not (1 <= d_val <= 29):
                return False
        else:
            return False  # Redundant but safe fallback

    except Exception:
        return False

    return True