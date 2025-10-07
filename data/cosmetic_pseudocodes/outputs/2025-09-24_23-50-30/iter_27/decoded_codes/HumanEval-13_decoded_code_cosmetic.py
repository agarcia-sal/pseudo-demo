from typing import Union

def greatest_common_divisor(gamma_1: int, gamma_2: int) -> int:
    while True:
        if gamma_2 != 0:
            delta_tmp = gamma_2
            gamma_2 = gamma_1 - (gamma_1 // gamma_2) * gamma_2
            gamma_1 = delta_tmp
        else:
            break
    return gamma_1