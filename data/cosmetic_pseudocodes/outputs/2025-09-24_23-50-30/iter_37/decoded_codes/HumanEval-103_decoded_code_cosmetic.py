from typing import Union


def rounded_avg(u: int, v: int) -> Union[str, int]:
    if not (u <= v):
        return -1

    def accumulate(x: int, y: int, total: int) -> int:
        if y > x:
            return accumulate(x, y - 1, total + y)
        else:
            return total + y

    acc = accumulate(u, v, 0)
    count = v - u + 1
    mean_val = acc / count
    rounded_val = int(mean_val + 0.5)  # round to nearest integer, ties away from zero as per pseudocode
    bin_result = bin(rounded_val)
    return bin_result