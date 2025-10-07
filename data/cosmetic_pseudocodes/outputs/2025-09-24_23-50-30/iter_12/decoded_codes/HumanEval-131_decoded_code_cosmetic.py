from typing import Callable

def digits(x: int) -> int:
    def loop(index: int, mul: int, cnt: int) -> int:
        s = str(x)
        if index >= len(s):
            return mul if cnt != 0 else 0
        num_digit = int(s[index])
        if num_digit % 2 != 0:
            return loop(index + 1, mul * num_digit, cnt + 1)
        else:
            return loop(index + 1, mul, cnt)
    return loop(0, 1, 0)