from typing import List

def fib4(n: int) -> int:
    base_values: List[int] = [0, 0, 2, 0]
    if n < 4:
        return base_values[n]

    for index in range(4, n + 1):
        next_value = base_values[-1] + base_values[-2] + base_values[-3] + base_values[-4]
        base_values.append(next_value)
        base_values.pop(0)

    return base_values[-1]