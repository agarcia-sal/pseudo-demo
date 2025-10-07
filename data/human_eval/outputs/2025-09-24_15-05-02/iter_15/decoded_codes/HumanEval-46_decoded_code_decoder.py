from typing import List

def fib4(n: int) -> int:
    results: List[int] = [0, 0, 2, 0]
    if n < 4:
        return results[n]
    for _ in range(4, n + 1):
        next_value = results[-1] + results[-2] + results[-3] + results[-4]
        results.append(next_value)
        results.pop(0)
    return results[-1]