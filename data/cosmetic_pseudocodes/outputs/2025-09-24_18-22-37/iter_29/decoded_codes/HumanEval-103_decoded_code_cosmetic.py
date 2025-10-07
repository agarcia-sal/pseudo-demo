from typing import Union


def rounded_avg(x: int, y: int) -> Union[str, int]:
    if x > y:
        return -1
    acc = 0
    idx = x
    while idx <= y:
        acc += idx
        idx += 1
    count = (y - x) + 1
    avg_val = acc / count
    round_val = round(avg_val)
    bin_str = bin(round_val)
    return bin_str