from typing import Optional


def valid_date(date_string: str) -> bool:
    cleaned: str = date_string.strip()
    parts: list[str] = cleaned.split('-')

    if len(parts) != 3:
        return False

    try:
        m: int = int(parts[0])
        d: int = int(parts[1])
        y: int = int(parts[2])
    except ValueError:
        return False

    if m < 1 or m > 12:
        return False

    if m in {1, 3, 5, 7, 8, 10, 12}:
        if d < 1 or d > 31:
            return False
    elif m in {4, 6, 9, 11}:
        if d < 1 or d > 30:
            return False
    elif m == 2:
        if d < 1 or d > 29:
            return False
    else:
        return False

    return True