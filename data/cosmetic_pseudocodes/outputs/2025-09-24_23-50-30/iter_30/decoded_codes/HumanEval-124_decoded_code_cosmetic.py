from typing import Union

def valid_date(token: Union[str, object]) -> bool:
    try:
        q: str = token.strip()  # Remove surrounding whitespace
        r, s, t = q.split('-')  # Expect format 'month-day-year' or similar
        u: int = int(r)  # Month
        v: int = int(s)  # Day
        w: int = int(t)  # Year (unused in validation but parsed)

        if u < 1 or u > 12:
            return False
        if u in {1, 3, 5, 7, 8, 10, 12} and (v < 1 or v > 31):
            return False
        if u in {4, 6, 9, 11} and (v < 1 or v > 30):
            return False
        if u == 2 and (v < 1 or v > 29):
            return False
    except Exception:
        return False

    return True