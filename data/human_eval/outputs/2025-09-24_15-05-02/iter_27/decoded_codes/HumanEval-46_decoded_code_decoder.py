from typing import List

def fib4(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be non-negative")
    results: List[int] = [0, 0, 2, 0]
    if n < 4:
        return results[n]
    for _ in range(4, n + 1):
        next_value: int = sum(results)
        results.append(next_value)
        results.pop(0)
    return results[-1]