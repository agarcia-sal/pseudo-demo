from typing import Optional


def rounded_avg(a: int, b: int) -> str:
    if not (a <= b):
        return "-1"

    def accumulate_sum(current: int, end: int, total: int) -> int:
        if current > end:
            return total
        else:
            return accumulate_sum(current + 1, end, total + current)

    total_sum: int = accumulate_sum(a, b, 0)
    count: int = (b - a) + 1
    raw_mean: float = total_sum / count
    rounded_mean: int = int((raw_mean + 0.5) // 1)
    binary_string: str = ""

    def to_binary(num: int) -> str:
        if num == 0:
            return "0"

        def rec_convert(x: int) -> str:
            if x == 0:
                return ""
            else:
                return rec_convert(x // 2) + str(x % 2)

        return rec_convert(num)

    binary_string = to_binary(rounded_mean)
    return binary_string