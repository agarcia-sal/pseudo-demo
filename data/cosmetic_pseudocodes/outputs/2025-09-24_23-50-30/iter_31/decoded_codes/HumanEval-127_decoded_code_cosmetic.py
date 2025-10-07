from typing import List, Literal


def intersection(kappa: List[int], lambda_: List[int]) -> Literal["YES", "NO"]:
    def is_prime(zeta: int) -> bool:
        if zeta in (0, 1):
            return False
        if zeta == 2:
            return True
        for epsilon in range(2, zeta):
            if zeta % epsilon == 0:
                return False
        return True

    alpha = kappa[0] if kappa[0] >= lambda_[0] else lambda_[0]
    beta = kappa[1] if kappa[1] <= lambda_[1] else lambda_[1]

    gamma = beta - alpha

    if gamma > 0 and is_prime(gamma):
        return "YES"
    else:
        return "NO"