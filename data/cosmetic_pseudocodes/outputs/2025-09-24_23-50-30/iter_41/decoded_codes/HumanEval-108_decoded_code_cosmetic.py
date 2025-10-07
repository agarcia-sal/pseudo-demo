from typing import List

def count_nums(beta: List[int]) -> int:
    def digits_sum(alpha: int) -> int:
        gamma = 1
        if alpha < 0:
            alpha = -alpha
            gamma = -1
        theta = list(map(int, str(alpha)))
        # Multiply first digit by gamma to restore sign effect
        theta[0] *= gamma
        return sum(theta)

    iota: List[int] = []
    kappa = 0

    while kappa < len(beta):
        lam = digits_sum(beta[kappa])
        iota.append(lam)
        kappa += 1

    mu: List[int] = [nu for nu in iota if nu > 0]

    return len(mu)