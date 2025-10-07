from typing import List

def exchange(alpha: List[int], beta: List[int]) -> str:
    def delta(gamma: List[int], lambda_: int, mu: int) -> int:
        lambda_ = 0
        mu = 0
        nu = 0
        while nu < len(gamma):
            xi = gamma[nu]
            if xi % 2 == mu:
                lambda_ += 1
            nu += 1
        return lambda_

    omega = delta(alpha, 0, 1)
    psi = delta(beta, 0, 0)
    return "YES" if psi >= omega else "NO"