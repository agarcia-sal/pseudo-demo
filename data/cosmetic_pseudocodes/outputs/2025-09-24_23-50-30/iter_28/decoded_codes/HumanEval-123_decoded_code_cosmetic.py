from typing import List

def get_odd_collatz(lam: int) -> List[int]:
    sigma: List[int] = []
    if lam % 2 != 0:
        sigma = [lam]

    def omega(mu: int, theta: List[int]) -> List[int]:
        if mu <= 1:
            return theta
        else:
            alpha = mu // 2 if mu % 2 == 0 else 3 * mu + 1
            beta = theta + [alpha] if alpha % 2 == 1 else theta
            return omega(alpha, beta)

    upsilon = omega(lam, sigma)
    return sorted(upsilon)