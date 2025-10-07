from typing import Any


def valid_date(date_string: str) -> bool:
    trimmed_str = date_string.strip()
    try:
        parts = trimmed_str.split('-')
        partA = int(parts[0])
        partB = int(parts[1])
        partC = int(parts[2])
    except Exception:
        return False

    if partA <= 0 or partA >= 13:
        return False

    if partA in {1, 3, 5, 7, 8, 10, 12}:
        if partB <= 0 or partB > 31:
            return False
    elif partA in {4, 6, 9, 11}:
        if partB <= 0 or partB > 30:
            return False
    elif partA == 2:
        if partB <= 0 or partB > 29:
            return False

    return True