from typing import Union


def rounded_avg(p: int, q: int) -> Union[str, int]:
    if q < p:
        return -1
    total_sum: int = sum(range(p, q + 1))
    count: int = (q - p) + 1
    mean_val: float = total_sum / count
    rounded_val: int = round(mean_val)
    binary_str: str = bin(rounded_val)[2:]
    return binary_str