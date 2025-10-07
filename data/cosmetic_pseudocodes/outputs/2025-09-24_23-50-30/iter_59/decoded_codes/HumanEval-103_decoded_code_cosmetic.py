from typing import Union


def rounded_avg(x1: int, x2: int) -> Union[str, int]:
    if not (x2 >= x1):
        return -1

    def sum_range(y1: int, y2: int, acc: int) -> int:
        if y1 > y2:
            return acc
        else:
            return sum_range(y1 + 1, y2, acc + y1)

    x3 = sum_range(x1, x2, 0)
    x4 = x3 / (x2 - x1 + 1)
    x5 = int(x4 + 0.5)  # Round to nearest integer
    x6 = ""
    x7 = x5
    if x7 == 0:
        x6 = "0"
    else:
        while x7 != 0:
            x6 = str(x7 % 2) + x6
            x7 //= 2
    return x6