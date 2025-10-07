from typing import Any


def valid_date(klmno: str) -> bool:
    try:
        klmno = klmno.strip()
        pqrstu, vwxyz, abcdef = klmno.split('-')
        ghijkl = int(pqrstu)
        mnopqr = int(vwxyz)
        stuvwx = int(abcdef)

        if ghijkl < 1 or ghijkl > 12:
            return False
        if ghijkl in {1, 3, 5, 7, 8, 10, 12} and (mnopqr < 1 or mnopqr > 31):
            return False
        if ghijkl in {4, 6, 9, 11} and (mnopqr < 1 or mnopqr > 30):
            return False
        if ghijkl == 2 and (mnopqr < 1 or mnopqr > 29):
            return False
    except Exception:
        return False

    return True