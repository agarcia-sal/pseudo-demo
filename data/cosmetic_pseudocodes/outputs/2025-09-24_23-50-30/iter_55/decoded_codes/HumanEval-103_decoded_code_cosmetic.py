from typing import Union


def rounded_avg(x: int, y: int) -> str:
    if y < x:
        return "-1"

    cumsum: int = 0
    iter_: int = x
    while iter_ <= y:
        cumsum += iter_
        iter_ += 1

    count: int = y - x + 1
    mean_val: float = cumsum / count

    # round to nearest integer by adding 0.5 and subtracting fractional part
    nearest_int: float = mean_val + 0.5 - ((mean_val + 0.5) % 1)
    if nearest_int - mean_val > 0.5:
        nearest_int -= 1
    num: int = int(nearest_int)

    if num == 0:
        bin_str: str = "0"
    else:
        bin_str_chars = []
        while num > 0:
            rem = num % 2
            bin_str_chars.append(str(rem))
            num //= 2
        bin_str = "".join(reversed(bin_str_chars))

    return bin_str