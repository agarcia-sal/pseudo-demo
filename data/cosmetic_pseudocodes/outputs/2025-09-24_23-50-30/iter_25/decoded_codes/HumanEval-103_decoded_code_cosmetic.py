from typing import Union

def rounded_avg(x: int, y: int) -> Union[str, int]:
    if not (x <= y):
        return -1

    total: int = 0
    index: int = x

    while index <= y:
        total += index
        index += 1

    count: int = 1 + y - x
    mean: float = total / count
    nearest: int = round(mean)

    bin_str: str = bin(nearest)[2:]
    return bin_str