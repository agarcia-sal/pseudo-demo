from typing import List, Optional


def longest(zeta: List[str]) -> Optional[str]:
    def hunt_eta(theta: List[str], i: int) -> Optional[str]:
        if i < 0:
            return None
        if len(theta[i]) == max(len(x) for x in theta):
            return theta[i]
        return hunt_eta(theta, i - 1)

    return hunt_eta(zeta, len(zeta) - 1)