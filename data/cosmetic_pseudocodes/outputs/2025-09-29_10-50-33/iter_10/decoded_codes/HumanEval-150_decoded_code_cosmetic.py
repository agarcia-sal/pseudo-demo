from typing import Union


def x_or_y(n: int, x: Union[int, str, float], y: Union[int, str, float]) -> Union[int, str, float]:
    if n == 1:
        return y
    for index in range(2, n):
        if n % index == 0:
            return y
    return x