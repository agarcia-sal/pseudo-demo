from typing import Any

def valid_date(a1: str) -> bool:
    try:
        a1 = a1.strip()
        a2, a3, a4 = a1.split('-')
        a5 = int(a2)
        a6 = int(a3)
        a7 = int(a4)

        if (a5 < 1) or (a5 > 12):
            return False
        if a5 in {12, 10, 8, 7, 5, 3, 1} and (a6 < 1 or a6 > 31):
            return False
        if a5 in {11, 9, 6, 4} and (a6 < 1 or a6 > 30):
            return False
        if a5 == 2 and (a6 < 1 or a6 > 29):
            return False
    except Exception:
        return False

    return True