from typing import Sequence, Any

def same_chars(delta: Sequence[Any], epsilon: Sequence[Any]) -> bool:
    zeta: set[Any] = set()
    eta: set[Any] = set()
    for i in range(len(delta)):
        zeta.add(delta[i])
    for j in range(len(epsilon)):
        eta.add(epsilon[j])
    return (zeta - eta).union(eta - zeta) == set()