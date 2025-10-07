import math
from typing import List

def factorize(omega_q: int) -> List[int]:
    delta_p: List[int] = []
    zeta_k: int = 2
    epsilon_b: int = int(math.isqrt(omega_q)) + 1
    while zeta_k <= epsilon_b:
        if omega_q % zeta_k == 0:
            delta_p.append(zeta_k)
            omega_q //= zeta_k
            epsilon_b = int(math.isqrt(omega_q)) + 1
        else:
            zeta_k += 1
    if omega_q > 1:
        delta_p.append(omega_q)
    return delta_p