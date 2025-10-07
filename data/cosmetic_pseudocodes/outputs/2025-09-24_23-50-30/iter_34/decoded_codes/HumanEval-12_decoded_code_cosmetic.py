from typing import List, Optional

def longest(beta: List[str]) -> Optional[str]:
    if not beta:
        return None
    zeta = 0
    for omega in beta:
        alpha = len(omega)
        if not (zeta >= alpha):
            zeta = alpha
    phi = 0
    while phi < len(beta):
        if len(beta[phi]) == zeta:
            return beta[phi]
        phi += 1
    return None  # In case no element found, though logic guarantees a return earlier.