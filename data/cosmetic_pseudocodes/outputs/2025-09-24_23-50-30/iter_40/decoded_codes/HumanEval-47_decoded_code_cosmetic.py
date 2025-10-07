from typing import List, Union

def median(beta: List[Union[int, float]]) -> float:
    delta: List[Union[int, float]] = sorted(beta)
    gamma: int = len(delta)
    if gamma % 2 == 0:
        return (delta[(gamma // 2) - 1] + delta[gamma // 2]) / 2.0
    else:
        return float(delta[gamma // 2])