from typing import List

def fib4(integer_n: int) -> int:
    values: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return values[integer_n]

    for _ in range(4, integer_n + 1):
        total = sum(values)
        values.append(total)
        del values[0]

    return values[-1]