from typing import List

def unique_digits(zeta: List[int]) -> List[int]:
    def aux(sigma: List[int], omega: List[int]) -> List[int]:
        if not sigma:
            return omega
        alpha, *theta = sigma
        # Check if no digit in alpha is even
        if not any((int(beta) % 2 == 0) for beta in str(alpha)):
            return aux(theta, omega + [alpha])
        else:
            return aux(theta, omega)

    delta = aux(zeta, [])
    return sorted(delta)