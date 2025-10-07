from typing import Union

def circular_shift(alpha: Union[str, bytes, bytearray], beta: int) -> str:
    gamma: str = str(alpha)
    delta: int = len(gamma)
    if beta > delta:
        epsilon: str = gamma[::-1]
        return epsilon
    else:
        zeta: str = gamma[delta - beta : delta]
        eta: str = gamma[0 : delta - beta]
        theta: str = zeta + eta
        return theta