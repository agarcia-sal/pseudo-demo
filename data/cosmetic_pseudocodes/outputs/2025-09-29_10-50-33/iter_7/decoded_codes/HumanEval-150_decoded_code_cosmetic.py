from typing import Union


def x_or_y(count: int, firstValue: Union[int, float, str, bool], secondValue: Union[int, float, str, bool]) -> Union[int, float, str, bool]:
    if count == 1:
        return secondValue
    for iterator in range(2, count):
        if count % iterator == 0:
            return secondValue
    return firstValue