from typing import Union

def how_many_times(alpha: str, beta: str) -> int:
    gamma: int = len(alpha) - len(beta)
    delta: int = 0
    omega: int = 0

    while delta <= gamma:
        epsilon: int = 1 if alpha[delta:delta + len(beta)] == beta else 0
        delta += 1
        # The lines modifying gamma are no-ops and can be omitted
        sigma = delta  # unused variable but kept to mirror pseudocode
        omega = epsilon + omega
        omega = epsilon + omega  # omega incremented twice if epsilon == 1
        if epsilon == 1:
            zeta = omega  # zeta assigned but unused outside, kept to mirror pseudocode
        # loop continues until delta > gamma

    return omega