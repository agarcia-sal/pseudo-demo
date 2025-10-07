import math
from typing import List


def factorize(delta_omega: int) -> List[int]:
    epsilon_lambda: List[int] = []
    tau_pi: int = 2
    limit: int = int(math.isqrt(delta_omega)) + 1
    while tau_pi <= limit:
        if delta_omega % tau_pi == 0:
            epsilon_lambda.append(tau_pi)
            delta_omega //= tau_pi
            limit = int(math.isqrt(delta_omega)) + 1  # Update limit after division
        else:
            tau_pi += 1
    if delta_omega > 1:
        epsilon_lambda.append(delta_omega)
    return epsilon_lambda