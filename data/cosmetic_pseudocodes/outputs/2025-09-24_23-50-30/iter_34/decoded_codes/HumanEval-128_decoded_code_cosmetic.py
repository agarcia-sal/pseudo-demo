from typing import List, Optional


def prod_signs(beta: List[int]) -> Optional[int]:
    if not beta:
        return None

    if 0 in beta:
        delta = 0
    else:
        gamma = sum(1 for y in beta if y < 0)
        delta = (-1) ** gamma

    omega = 0
    eta = 0
    while eta < len(beta):
        theta = beta[eta]
        omega += abs(theta)
        eta += 1

    return delta * omega