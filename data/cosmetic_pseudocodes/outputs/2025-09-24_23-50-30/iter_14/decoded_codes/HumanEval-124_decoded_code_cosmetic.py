from typing import Optional


def valid_date(date_string: str) -> bool:
    date_str = date_string.strip()
    parts = date_str.split('-')
    if len(parts) != 3:
        return False

    try:
        a = int(parts[0])
        b = int(parts[1])
        c = int(parts[2])
    except ValueError:
        return False

    if a < 1 or a > 12:
        return False

    months_31 = {1, 3, 5, 7, 8, 10, 12}
    months_30 = {4, 6, 9, 11}

    if a in months_31:
        if b < 1 or b > 31:
            return False
    elif a in months_30:
        if b < 1 or b > 30:
            return False
    elif a == 2:
        if b < 1 or b > 29:
            return False

    return True