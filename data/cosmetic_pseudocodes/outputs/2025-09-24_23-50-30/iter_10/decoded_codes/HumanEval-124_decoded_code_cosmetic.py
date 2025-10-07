from typing import Any


def valid_date(alpha: str) -> bool:
    beta = alpha.strip()
    try:
        parts = beta.split('-')
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])

        if x < 1 or x > 12:
            return False
        if x in {1, 3, 5, 7, 8, 10, 12} and (y < 1 or y > 31):
            return False
        if x in {4, 6, 9, 11} and (y < 1 or y > 30):
            return False
        if x == 2 and (y < 1 or y > 29):
            return False
    except Exception:
        return False
    return True