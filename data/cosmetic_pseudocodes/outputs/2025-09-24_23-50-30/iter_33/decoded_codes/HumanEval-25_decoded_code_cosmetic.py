import math
from typing import List

def factorize(parameter_alpha: int) -> List[int]:
    container_sigma: List[int] = []
    cursor_mu: int = 2
    bound_theta: int = int(math.isqrt(parameter_alpha)) + 1

    while cursor_mu <= bound_theta:
        if parameter_alpha % cursor_mu == 0:
            container_sigma.append(cursor_mu)
            parameter_alpha //= cursor_mu
        else:
            cursor_mu += 1
        bound_theta = int(math.isqrt(parameter_alpha)) + 1

    if parameter_alpha > 1:
        container_sigma.append(parameter_alpha)

    return container_sigma