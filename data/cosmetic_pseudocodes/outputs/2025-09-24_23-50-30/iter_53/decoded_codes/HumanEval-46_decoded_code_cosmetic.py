from typing import List

def fib4(alpha: int) -> int:
    omega: List[int] = [0, 0, 2, 0]
    if alpha < 4:
        return omega[alpha]

    def lambda_(delta: int, sigma: int) -> int:
        nonlocal omega
        if delta > sigma:
            return omega[3]
        tau = sum(omega)
        omega.pop(0)
        omega.append(tau)
        return lambda_(delta + 1, sigma)

    return lambda_(4, alpha)