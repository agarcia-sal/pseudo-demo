from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> Union[str, int]:
    if integer_m < integer_n:
        return -1
    accumulator: int = 0
    current: int = integer_n
    while current <= integer_m:
        accumulator += current
        current += 1
    count: int = (integer_m - integer_n) + 1
    mean: float = accumulator / count
    nearest_int: int = round(mean)
    return bin(nearest_int)