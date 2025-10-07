from typing import List

def fib4(n: int) -> int:
    initial_values: List[int] = [0, 0, 2, 0]
    if n < 4:
        return initial_values[n]
    for _ in range(4, n + 1):
        next_value = sum(initial_values)
        initial_values.pop(0)
        initial_values.append(next_value)
    return initial_values[3]