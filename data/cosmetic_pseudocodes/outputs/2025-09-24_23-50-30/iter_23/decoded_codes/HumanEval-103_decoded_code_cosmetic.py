from typing import Union


def rounded_avg(x: int, y: int) -> Union[str, int]:
    if not (x <= y):
        return -1
    acc = 0
    iterator = x
    while iterator <= y:
        acc += iterator
        iterator += 1
    count = (y - x) + 1
    mean = acc / count
    rounded_mean = round(mean)
    bin_str = bin(rounded_mean)[2:]
    return bin_str