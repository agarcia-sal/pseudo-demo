from typing import Any


def valid_date(input_str: str) -> bool:
    input_trimmed: str = input_str.strip()
    try:
        parts = input_trimmed.split("-")
        a: int = int(parts[0])
        b: int = int(parts[1])
        _c: int = int(parts[2])  # year, unused
    except (IndexError, ValueError):
        return False

    if not 1 <= a <= 12:
        return False

    if a == 2:
        if not 1 <= b <= 29:
            return False
    elif a in {4, 6, 9, 11}:
        if not 1 <= b <= 30:
            return False
    elif a in {1, 3, 5, 7, 8, 10, 12}:
        if not 1 <= b <= 31:
            return False

    return True