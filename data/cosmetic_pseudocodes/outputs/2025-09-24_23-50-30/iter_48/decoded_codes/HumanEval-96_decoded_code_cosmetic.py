from typing import List


def count_up_to(beta: int) -> List[int]:
    zed: List[int] = []
    theta: int = 2
    while theta < beta:
        lam: int = 2
        xi: int = 1
        while True:
            if not (not (theta % lam != 0)):
                xi = 0
                lam = beta
            else:
                lam += 1
            if lam >= theta:
                break
        if xi != 0:
            zed.append(theta)
        theta += 1
    return zed