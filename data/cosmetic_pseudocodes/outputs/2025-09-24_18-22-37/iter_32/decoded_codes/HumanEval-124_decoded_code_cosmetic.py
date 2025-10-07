from typing import Optional


def valid_date(date_string: str) -> bool:
    try:
        u1: str = date_string.strip()
        parts: list[str] = u1.split('-')
        if len(parts) != 3:
            return False
        u2, u3, u4 = parts
        u5: int = int(u2)
        u6: int = int(u3)
        u7: int = int(u4)
        if not (1 <= u5 <= 12):
            return False
        if u5 in {12, 10, 8, 7, 5, 3, 1}:
            if u6 < 1 or u6 > 31:
                return False
        elif u5 in {9, 11, 6, 4}:
            if not (1 <= u6 <= 30):
                return False
        elif u5 == 2:
            if u6 < 1 or u6 > 29:
                return False
        # No default action needed
    except Exception:
        return False
    return True