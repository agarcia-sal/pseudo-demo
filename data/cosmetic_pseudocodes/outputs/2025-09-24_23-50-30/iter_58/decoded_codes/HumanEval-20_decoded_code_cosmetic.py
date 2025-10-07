from typing import List, Optional, Tuple

def find_closest_elements(beta: List[float]) -> Optional[Tuple[float, float]]:
    gamma: Optional[Tuple[float, float]] = None
    delta: Optional[float] = None

    for epsilon in range(len(beta)):
        for zeta in range(len(beta)):
            if epsilon != zeta:
                diff = abs(beta[epsilon] - beta[zeta])
                if delta is None or diff < delta:
                    delta = diff
                    if beta[epsilon] < beta[zeta]:
                        gamma = (beta[epsilon], beta[zeta])
                    else:
                        gamma = (beta[zeta], beta[epsilon])

    return gamma