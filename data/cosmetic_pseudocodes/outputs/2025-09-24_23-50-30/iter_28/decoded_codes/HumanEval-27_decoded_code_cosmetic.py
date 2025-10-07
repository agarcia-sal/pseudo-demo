from typing import Callable

def flip_case(beta: str) -> str:
    def aux(alpha: str, omega: str) -> str:
        if len(alpha) == 0:
            return omega
        else:
            delta = alpha[0]
            epsilon = alpha[1:]
            if 'a' <= delta <= 'z':
                zeta = delta.upper()
            elif 'A' <= delta <= 'Z':
                zeta = delta.lower()
            else:
                zeta = delta
            return aux(epsilon, omega + zeta)
    return aux(beta, "")