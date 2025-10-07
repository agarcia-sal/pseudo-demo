from typing import Union

def is_simple_power(x: Union[int, float], n: Union[int, float]) -> bool:
    if n == 1:
        return x == 1
    power = 1
    while power < x:
        power *= n
    return power == x