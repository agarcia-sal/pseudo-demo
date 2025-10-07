from typing import List, Union
from math import floor

def median(alpha: List[Union[int, float]]) -> float:
    def helper(beta: List[Union[int, float]], gamma: int) -> Union[int, float]:
        if gamma == 0:
            return beta[0]
        else:
            return helper(beta[1:], gamma - 1)

    sorted_alpha = sorted(alpha)
    half_index = floor(len(alpha) / 2)
    delta = helper(sorted_alpha, half_index)
    epsilon = len(alpha) % 2

    if epsilon == 1:
        return float(delta)
    else:
        eta = helper(sorted_alpha, half_index - 1)
        return (delta + eta) / 2.0