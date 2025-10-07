from typing import Optional


def valid_date(date_string: str) -> bool:
    try:
        trimmed_string: str = date_string.strip()
        parts_list: list[str] = trimmed_string.split('-')
        if len(parts_list) != 3:
            return False

        a: int = int(parts_list[0])
        b: int = int(parts_list[1])
        c: int = int(parts_list[2])

        if not (1 <= a <= 12):
            return False

        months_31 = {1, 3, 5, 7, 8, 10, 12}
        months_30 = {4, 6, 9, 11}

        if a in months_31:
            if not (1 <= b <= 31):
                return False
        elif a in months_30:
            if not (1 <= b <= 30):
                return False
        elif a == 2:
            if not (1 <= b <= 29):
                return False

    except Exception:
        return False

    return True