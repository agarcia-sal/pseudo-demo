from typing import Union

def multiply(alpha: Union[int, float], beta: Union[int, float]) -> float:
    delta: float = alpha - (alpha // 10 * 10)
    epsilon: float = beta - (beta // 10 * 10)
    if delta < 0:
        delta = -delta
    if epsilon < 0:
        epsilon = -epsilon
    return delta * epsilon