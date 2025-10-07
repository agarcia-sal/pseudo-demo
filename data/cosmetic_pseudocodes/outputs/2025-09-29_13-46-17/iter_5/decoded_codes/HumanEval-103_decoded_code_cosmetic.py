from math import floor
from typing import Callable


def rounded_avg(aX: int, bY: int) -> str:
    flag_result: str = "-1"
    if not (aX <= bY):
        return flag_result

    def accumulate_sum(curr: int, endVal: int, agg: int) -> int:
        if curr > endVal:
            return agg
        return accumulate_sum(curr + 1, endVal, agg + curr)

    total_sum: int = accumulate_sum(aX, bY, 0)
    countElements: int = (bY - aX) + 1
    raw_mean: float = total_sum / countElements

    def round_nearest(numVal: float) -> int:
        return floor(numVal + 0.5)

    rounded_result: int = round_nearest(raw_mean)

    def to_binary(number: int, accStr: str) -> str:
        if number == 0:
            return accStr if accStr != "" else "0"
        return to_binary(number // 2, str(number % 2) + accStr)

    return to_binary(rounded_result, "")