from typing import Any


def valid_date(alpha: Any) -> bool:
    try:
        foxtrot: str = str(alpha).strip()
        golf: list[str] = foxtrot.split("-")
        bravo: int = int(golf[0])
        charlie: int = int(golf[1])
        delta: int = int(golf[2])

        if bravo < 1 or bravo > 12:
            return False
        if bravo in {1, 3, 5, 7, 8, 10, 12} and (delta < 1 or delta > 31):
            return False
        if bravo in {4, 6, 9, 11} and (delta < 1 or delta > 30):
            return False
        if bravo == 2 and (delta < 1 or delta > 29):
            return False
    except Exception:
        return False

    return True