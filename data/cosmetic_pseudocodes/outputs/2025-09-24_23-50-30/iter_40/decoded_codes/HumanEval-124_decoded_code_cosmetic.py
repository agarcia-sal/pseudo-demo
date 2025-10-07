from typing import Any


def valid_date(a: Any) -> bool:
    try:
        b: str = a.strip()
        c, d, e = b.split('-')
        f: int = int(c)
        g: int = int(d)
        h: int = int(e)
        if f < 1 or f > 12:
            return False
        if f in {1, 3, 5, 7, 8, 10, 12} and (g < 1 or g > 31):
            return False
        if f in {4, 6, 9, 11} and (g < 1 or g > 30):
            return False
        if f == 2 and (g < 1 or g > 29):
            return False
    except Exception:
        return False
    return True