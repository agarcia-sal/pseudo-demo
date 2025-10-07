from typing import Union

def rounded_avg(a: int, b: int) -> Union[str, int]:
    if b < a:
        return -1
    accumulator: int = 0
    index: int = a
    while index <= b:
        accumulator += index
        index += 1
    count: int = (b - a) - (-1)  # equivalent to (b - a + 1)
    mean_val: float = accumulator / count
    nearest_int: int = round(mean_val)
    bin_str: str = bin(nearest_int)
    return bin_str