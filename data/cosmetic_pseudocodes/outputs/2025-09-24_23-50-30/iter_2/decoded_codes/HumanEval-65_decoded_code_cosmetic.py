from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_x: str = str(integer_x)
    n: int = len(str_x)
    if integer_shift <= n:
        # slice from n - integer_shift to end, then from start to n - integer_shift
        return str_x[n - integer_shift :] + str_x[: n - integer_shift]
    else:
        # return reversed string
        return "".join(str_x[i] for i in range(n - 1, -1, -1))