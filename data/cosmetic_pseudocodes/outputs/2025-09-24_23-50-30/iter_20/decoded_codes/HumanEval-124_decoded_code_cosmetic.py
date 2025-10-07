from typing import Any


def valid_date(xyz: Any) -> bool:
    try:
        x1 = str(xyz).strip()
        x2, x3, x4 = x1.split('-')
        a = int(x2)
        b = int(x3)
        c = int(x4)
    except Exception:
        return False

    if not (1 <= a <= 12):
        return False

    if a in {1, 3, 5, 7, 8, 10, 12}:
        if not (1 <= b <= 31):
            return False
    elif a in {4, 6, 9, 11}:
        if not (1 <= b <= 30):
            return False
    elif a == 2:
        if not (1 <= b <= 29):
            return False

    return True