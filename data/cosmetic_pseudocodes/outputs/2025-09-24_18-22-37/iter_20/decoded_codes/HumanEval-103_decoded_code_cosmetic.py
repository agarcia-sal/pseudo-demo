from typing import Union

def rounded_avg(p: int, q: int) -> Union[str, int]:
    delta: int = q - p
    if delta < 0:
        return -1

    acc: int = 0
    idx: int = p
    while idx <= q:
        acc += idx
        idx += 1

    length: int = delta + 1
    quotient: float = acc / length
    rounded_res: int = round(quotient)
    bin_str: str = bin(rounded_res)[2:]

    return bin_str