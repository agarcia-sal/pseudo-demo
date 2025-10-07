from typing import Union

def sum_to_n(n: Union[int, float]) -> Union[int, float]:
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be an int or float")
    if n < 0:
        raise ValueError("Input must be non-negative")
    return sum(range(int(n) + 1))