from typing import Any


def valid_date(w: str) -> bool:
    try:
        x = w.strip()
        a, b, c = x.split('-')
        d = int(a)
        e = int(b)
        f = int(c)

        if d < 1 or d > 12:
            return False

        if d in {1, 3, 5, 7, 8, 10, 12} and (e < 1 or e > 31):
            return False

        if d in {4, 6, 9, 11} and (e < 1 or e > 30):
            return False

        if d == 2 and (e < 1 or e > 29):
            return False

    except Exception:
        return False

    return True