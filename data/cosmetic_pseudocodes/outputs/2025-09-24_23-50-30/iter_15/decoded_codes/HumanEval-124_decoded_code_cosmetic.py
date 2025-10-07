from typing import List

def valid_date(tau: str) -> bool:
    tau = tau.strip()
    psi: List[str] = tau.split('-')
    if len(psi) != 3:
        return False

    try:
        alpha = int(psi[0])
        beta = int(psi[1])
        gamma = int(psi[2])
    except ValueError:
        return False

    if not (1 <= alpha <= 12):
        return False

    valid_months_31 = {1, 3, 5, 7, 8, 10, 12}
    valid_months_30 = {4, 6, 9, 11}

    if alpha in valid_months_31:
        if not (1 <= beta <= 31):
            return False
    elif alpha in valid_months_30:
        if not (1 <= beta <= 30):
            return False
    elif alpha == 2:
        if not (1 <= beta <= 29):
            return False
    else:
        return False

    return True