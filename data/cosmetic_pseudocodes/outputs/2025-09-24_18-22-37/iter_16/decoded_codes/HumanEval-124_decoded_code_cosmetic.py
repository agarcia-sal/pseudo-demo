from typing import Any


def valid_date(alpha: str) -> bool:
    try:
        omega: str = alpha.strip()
        parts: list[str] = omega.split('-')
        p: str = parts[0]
        q: str = parts[1]
        r: str = parts[2]
        m: int = int(p)
        n: int = int(q)
        o: int = int(r)

        if m < 1 or m > 12:
            return False

        months_31 = {1, 3, 5, 7, 8, 10, 12}
        months_30 = {4, 6, 9, 11}

        if m in months_31:
            if n < 1 or n > 31:
                return False
        elif m in months_30:
            if n < 1 or n > 30:
                return False
        elif m == 2:
            if n < 1 or n > 29:
                return False
        else:  # month outside valid ranges
            return False

    except (IndexError, ValueError, TypeError):
        return False

    return True