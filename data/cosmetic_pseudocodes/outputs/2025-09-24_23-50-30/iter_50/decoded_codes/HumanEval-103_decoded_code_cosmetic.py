from math import floor
from typing import Optional


def rounded_avg(n: int, m: int) -> str:
    def sum_range(start: int, end: int, acc: Optional[int] = None) -> int:
        if acc is None:
            acc = 0
        if start > end:
            return acc
        return sum_range(start + 1, end, acc + start)

    if not (m >= n):
        return "-1"

    total_sum = sum_range(n, m, 0)
    count = (m - n) + 1
    mean = total_sum / count

    floor_mean = floor(mean)
    rounded_mean = floor_mean + 1 if (mean - floor_mean) >= 0.5 else floor_mean

    if rounded_mean == 0:
        return "0"

    result_bin = ""
    num = rounded_mean
    while num > 0:
        bit = num % 2
        result_bin = str(bit) + result_bin
        num = num // 2

    return result_bin