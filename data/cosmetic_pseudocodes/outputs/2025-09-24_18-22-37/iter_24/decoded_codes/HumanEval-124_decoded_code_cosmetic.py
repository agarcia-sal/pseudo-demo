from typing import Any


def valid_date(xyz: str) -> bool:
    try:
        abc = xyz.strip()
        p1, p2, p3 = abc.split('-')
        m = int(p1)
        d = int(p2)
        y = int(p3)

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

    except Exception:
        return False

    return True