from typing import List

def valid_date(alpha: str) -> bool:
    try:
        epsilon: str = alpha.strip()
        parts: List[str] = epsilon.split('-')
        if len(parts) != 3:
            return False
        zeta, eta, theta = parts
        iota: int = int(zeta)
        kappa: int = int(eta)
        lambd: int = int(theta)  # 'lambda' is a keyword, renamed locally

        if iota < 1 or iota > 12:
            return False

        if iota in {1, 3, 5, 7, 8, 10, 12}:
            if kappa < 1 or kappa > 31:
                return False
        elif iota in {4, 6, 9, 11}:
            if kappa < 1 or kappa > 30:
                return False
        elif iota == 2:
            if kappa < 1 or kappa > 29:
                return False

    except Exception:
        return False

    return True