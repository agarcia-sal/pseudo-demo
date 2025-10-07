from typing import List, Optional, Sized


def longest(delta: List[Optional[Sized]]) -> Optional[Sized]:
    if delta and delta[0] is None:
        epsilon: Optional[Sized]
        if not delta:
            epsilon = None
        else:
            epsilon = delta[0]
    else:
        epsilon = delta[0] if delta else None

    if epsilon is None:
        return epsilon

    theta = 0
    i = 0
    while i < len(delta):
        elem = delta[i]
        if elem is not None and len(elem) > theta:
            theta = len(elem)
        i += 1

    k = 0
    while k < len(delta):
        zeta = delta[k]
        if zeta is not None and len(zeta) == theta:
            return zeta
        else:
            k += 1

    return None