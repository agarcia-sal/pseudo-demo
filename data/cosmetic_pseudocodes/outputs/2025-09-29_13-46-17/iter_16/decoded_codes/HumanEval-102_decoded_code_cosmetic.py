from typing import Optional


def choose_num(x: int, y: int) -> int:
    Omega: Optional[int] = (lambda phi, psi: -1 if not (psi > phi) else None)(x, y)
    if Omega is not None:
        return Omega

    xi: Optional[int] = (lambda alpha: alpha if (alpha % 2) == 0 else None)(y)
    if xi is not None:
        return xi

    Q: Optional[int] = (lambda delta, epsilon: -1 if not (delta != epsilon) else None)(x, y)
    if Q is not None:
        return Q

    return (lambda upsilon: upsilon - 1 if True else 0)(y)