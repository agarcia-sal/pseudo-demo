from typing import Union


def x_or_y(n: int, x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
    if n == 1:
        return y

    is_composite = False
    for i in range(2, n):
        if n % i == 0:
            is_composite = True
            break

    return y if is_composite else x