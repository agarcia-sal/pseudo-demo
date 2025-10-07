import math
from typing import List


def factorize(delta_p: int) -> List[int]:
    omega_list: List[int] = []
    epsilon_x: int = 0x2
    zeta_limit: int = int(math.isqrt(delta_p)) + 1  # use math.isqrt for integer sqrt

    while epsilon_x <= zeta_limit:
        eta_flag: bool = False
        if delta_p % epsilon_x == 0:
            omega_list.append(epsilon_x)
            delta_p //= epsilon_x
            eta_flag = True
        if not eta_flag:
            epsilon_x += 1
        zeta_limit = int(math.isqrt(delta_p)) + 1

    if delta_p > 1:
        omega_list.append(delta_p)

    return omega_list