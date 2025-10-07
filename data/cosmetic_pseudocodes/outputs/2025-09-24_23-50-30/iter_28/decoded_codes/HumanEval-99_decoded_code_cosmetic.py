from math import ceil, floor
from typing import Callable

def closest_integer(alpha: str) -> int:
    def trim_trailing_zeros(beta: str) -> str:
        # The original IF condition is obscure and appears to check if there is exactly one '.' in beta.
        # Count of '.' must be exactly 1 to proceed trimming trailing zeros.
        if beta.count('.') != 1:
            return beta

        def recur_trim(gamma: str) -> str:
            if not gamma:
                return gamma
            if gamma[-1] == '0':
                return recur_trim(gamma[:-1])
            return gamma

        return recur_trim(beta)

    delta = trim_trailing_zeros(alpha)
    epsilon = float(delta)

    if delta[-2:] == '.5':
        zeta = int(ceil(epsilon)) if epsilon > 0 else int(floor(epsilon))
    else:
        zeta = round(epsilon) if len(delta) > 0 else 0

    return int(zeta)