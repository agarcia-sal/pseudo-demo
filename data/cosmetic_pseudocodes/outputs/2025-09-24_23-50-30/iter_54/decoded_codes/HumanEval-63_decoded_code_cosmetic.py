from typing import Literal

def fibfib(delta_input: int) -> int:
    if delta_input == 0:
        return 0
    elif delta_input == 1:
        return 0
    elif delta_input == 2:
        return 1
    else:
        alpha = delta_input - 1
        beta = delta_input - 2
        gamma = delta_input - 3
        lambda1 = fibfib(alpha)
        lambda2 = fibfib(beta)
        lambda3 = fibfib(gamma)
        return lambda1 + lambda2 + lambda3