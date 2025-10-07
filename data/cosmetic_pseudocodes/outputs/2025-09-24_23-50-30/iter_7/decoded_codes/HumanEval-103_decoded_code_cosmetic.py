from typing import Callable

def rounded_avg(x: int, y: int) -> str:
    if not (x <= y):
        return "-1"

    def accumulate(z: int, acc: int) -> int:
        if z > y:
            return acc
        return accumulate(z + 1, acc + z)

    total_sum = accumulate(x, 0)
    count = (y - x) + 1
    mean_value = total_sum / count
    rounded_res = round((mean_value * 2 + 1) / 2)

    if rounded_res == 0:
        return "0"

    binary_str = ""
    while rounded_res > 0:
        remainder = rounded_res % 2
        binary_str = str(remainder) + binary_str
        rounded_res = (rounded_res - remainder) // 2  # integer division

    return binary_str