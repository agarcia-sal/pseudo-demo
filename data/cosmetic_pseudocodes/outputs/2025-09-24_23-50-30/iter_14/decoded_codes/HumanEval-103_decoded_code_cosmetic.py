from typing import Callable


def rounded_avg(a: int, b: int) -> str:
    if a > b:
        return "-1"

    def sum_range(x: int, y: int, acc: int) -> int:
        if x > y:
            return acc
        return sum_range(x + 1, y, acc + x)

    total: int = sum_range(a, b, 0)
    count: int = b - a + 1
    mean: float = total / count
    rounded: int = int(mean + 0.5)

    if rounded == 0:
        return "0"

    bin_str = ""
    value = rounded
    while value > 0:
        bit = value % 2
        bin_str = str(bit) + bin_str
        value = (value - bit) // 2

    return bin_str