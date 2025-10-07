from typing import Union

def is_simple_power(x: int, n: int) -> bool:
    if n == 1:
        return x == 1
    if x < 1 or n < 1:
        raise ValueError("Both x and n must be positive integers.")

    power: int = 1
    while power < x:
        power *= n

    return power == x