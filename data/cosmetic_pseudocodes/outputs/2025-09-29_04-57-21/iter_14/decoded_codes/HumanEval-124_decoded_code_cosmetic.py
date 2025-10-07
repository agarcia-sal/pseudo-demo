from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed_date: str = date_string.strip()
        parts: list[str] = trimmed_date.split('-')
        mon_text: str = parts[0]
        d_text: str = parts[1]
        y_text: str = parts[2]

        mon_num: int = int(mon_text)
        d_num: int = int(d_text)
        y_num: int = int(y_text)

        if not (1 <= mon_num <= 12):
            return False

        if mon_num == 2:
            if d_num < 1 or d_num > 29:
                return False
        else:
            if mon_num in {4, 6, 9, 11}:
                if not (1 <= d_num <= 30):
                    return False
            else:
                if d_num < 1 or d_num > 31:
                    return False
    except Exception:
        return False

    return True