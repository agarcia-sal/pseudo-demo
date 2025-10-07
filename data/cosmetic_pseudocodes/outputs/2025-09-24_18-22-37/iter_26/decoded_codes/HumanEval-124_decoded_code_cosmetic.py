from typing import Any


def valid_date(gamma_string: str) -> bool:
    gamma_string = gamma_string.strip()
    try:
        eps1, eps2, eps3 = gamma_string.split('-')
        eta = int(eps1)
        theta = int(eps2)
        iota = int(eps3)
    except Exception:
        return False

    if 1 <= eta <= 12:
        if eta in {1, 3, 5, 7, 8, 10, 12}:
            if theta < 1 or theta > 31:
                return False
        elif eta in {4, 6, 9, 11}:
            if theta < 1 or theta > 30:
                return False
        elif eta == 2:
            if theta < 1 or theta > 29:
                return False
        else:
            return False
        return True
    else:
        return False