from typing import Optional, Iterable, Hashable

def next_smallest(zeta: Iterable[Hashable]) -> Optional[Hashable]:
    omega: dict[Hashable, bool] = {}
    for eta in zeta:
        omega[eta] = True
    theta = sorted(omega.keys())
    if len(theta) < 2:
        return None
    return theta[1]