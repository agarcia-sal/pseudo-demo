import math
from typing import Sequence

def max_fill(delta: Sequence[float], alpha: float) -> int:
    omega: float = 0
    sigma: float = 0
    theta: int = 0
    while theta < len(delta):
        sigma += delta[theta]
        theta += 1
    omega = sigma / alpha
    return math.ceil(omega)