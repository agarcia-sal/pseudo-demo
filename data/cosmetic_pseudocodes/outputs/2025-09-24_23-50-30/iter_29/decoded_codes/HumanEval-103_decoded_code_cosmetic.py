from typing import Union

def rounded_avg(x: int, y: int) -> str:
    if y < x:
        return "-1"
    acc: int = 0
    idx: int = x
    while idx <= y:
        acc += idx
        idx += 1
    count: int = (y - x) + 1
    avg: float = acc / count
    rounded: int = round(avg)
    binary_str: str = bin(rounded)[2:]
    return binary_str