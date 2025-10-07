from typing import Union


def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1
    acc: int = 0
    idx: int = n
    while idx <= m:
        acc += idx
        idx += 1
    count: int = (m - n) + 1
    mean_val: float = acc / count
    rounded_val: int = round(mean_val)
    bin_str: str = bin(rounded_val)[2:]
    return bin_str