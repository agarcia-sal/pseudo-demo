from typing import Any


def any_int(eta: Any, theta: Any, kappa: Any) -> bool:
    if all(isinstance(x, int) for x in (eta, theta, kappa)):
        if (kappa == eta + theta) or (theta == eta + kappa) or (eta == theta + kappa):
            return True
        else:
            return False
    return False