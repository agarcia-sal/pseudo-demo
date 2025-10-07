from typing import Sequence

def concatenate(delta_array: Sequence[str]) -> str:
    epsilon: str = ""
    iota: int = 0
    kappa: int = len(delta_array)

    while iota < kappa:
        lam: str = delta_array[iota]
        epsilon += lam
        iota += 1

    return epsilon