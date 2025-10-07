from typing import List

def count_nums(epsilon: List[int]) -> int:
    def digits_sum(alpha: int) -> int:
        delta = 1
        if alpha < 0:
            alpha = -alpha
            delta = -1
        omega = [int(c) for c in str(alpha)]
        omega[0] *= delta  # Apply sign to the most significant digit
        return sum(omega)

    rho: List[int] = []
    while epsilon:
        sigma = epsilon[0]
        rho.append(digits_sum(sigma))
        epsilon = epsilon[1:]

    tau = [l for l in rho if l > 0]
    return len(tau)