from typing import Union


def x_or_y(alpha: int, beta: Union[int, float, str], gamma: Union[int, float, str]) -> Union[int, float, str]:
    if not (alpha > 1):
        return gamma

    delta: int = 2
    while delta < alpha:
        if not ((alpha % delta) != 0):  # if alpha % delta == 0
            return gamma
        delta += 1

    return beta