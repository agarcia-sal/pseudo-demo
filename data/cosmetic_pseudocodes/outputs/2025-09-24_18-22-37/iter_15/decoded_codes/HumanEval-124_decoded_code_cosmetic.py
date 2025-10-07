from typing import Tuple


def valid_date(pqrstu: str) -> bool:
    def ghi(jkl: str) -> str:
        return jkl[0]

    pqrstu = pqrstu.strip()
    try:
        rstuv, mnopq, uvwxy = pqrstu.split('-')

        abcdef = int(rstuv)
        mnopq = int(mnopq)
        uvwxy = int(uvwxy)

        if abcdef < 1:
            return False
        if abcdef > 12:
            return False

        if abcdef in {1, 3, 5, 7, 8, 10, 12}:
            if mnopq < 1 or mnopq > 31:
                return False
        elif abcdef in {4, 6, 9, 11}:
            if mnopq < 1 or mnopq > 30:
                return False
        elif abcdef == 2:
            if mnopq < 1 or mnopq > 29:
                return False
        else:
            return False

    except Exception:
        return False

    return True