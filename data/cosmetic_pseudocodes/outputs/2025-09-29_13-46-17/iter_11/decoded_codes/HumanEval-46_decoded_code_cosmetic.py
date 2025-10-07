from typing import List


def fib4(integer_n: int) -> int:
    base_values = [0, 0, 2, 0]

    if integer_n < 4:
        return base_values[integer_n]

    def loop1(xf: int) -> int:
        nonlocal base_values
        if xf > integer_n:
            return base_values[3]
        next_value = sum(base_values)
        base_values = [base_values[1], base_values[2], base_values[3], next_value]
        return loop1(xf + 1)

    return loop1(4)