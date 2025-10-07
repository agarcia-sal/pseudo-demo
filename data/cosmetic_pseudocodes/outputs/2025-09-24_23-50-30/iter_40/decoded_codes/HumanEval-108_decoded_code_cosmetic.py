from typing import Iterable, List


def count_nums(alpha: Iterable[int]) -> int:
    def digits_sum(beta: int) -> int:
        gamma = 1
        if beta < 0:
            beta = -beta
            gamma = -1
        delta: List[int] = [int(ch) for ch in str(beta)]
        delta[0] *= gamma  # apply sign to the most significant digit
        epsilon = sum(delta)
        return epsilon

    eta: List[int] = [digits_sum(theta) for theta in alpha]
    kappa: List[int] = [lam for lam in eta if lam > 0]
    return len(kappa)