from typing import List

def fib4(integer_n: int) -> int:
    initial_results: List[int] = [0, 0, 2, 0]
    if integer_n < 0:
        raise ValueError("integer_n must be non-negative")
    if integer_n < 4:
        return initial_results[integer_n]
    for _ in range(4, integer_n + 1):
        next_val = sum(initial_results)
        initial_results.append(next_val)
        initial_results.pop(0)
    return initial_results[-1]