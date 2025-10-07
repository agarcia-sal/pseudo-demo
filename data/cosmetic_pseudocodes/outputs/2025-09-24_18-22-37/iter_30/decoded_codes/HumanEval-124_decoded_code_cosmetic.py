from typing import List


def valid_date(alpha: str) -> bool:
    try:
        beta: str = alpha.lstrip()
        eta: str = beta.rstrip()
        iota: List[str] = eta.split('-')

        gamma: str = iota[0]
        delta: str = iota[1]
        epsilon: str = iota[2]

        zeta: int = int(gamma)
        theta: int = int(delta)
        eta_int: int = int(epsilon)  # 'eta' reused as int, renamed internally for clarity

        if zeta < 1:
            return False

        if zeta > 12:
            return False

        if zeta in {1, 3, 5, 7, 8, 10, 12}:
            if theta < 1 or theta > 31:
                return False

        if zeta in {4, 6, 9, 11}:
            if theta < 1 or theta > 30:
                return False

        if zeta == 2:
            if theta < 1 or theta > 29:
                return False

    except Exception:
        return False

    return True