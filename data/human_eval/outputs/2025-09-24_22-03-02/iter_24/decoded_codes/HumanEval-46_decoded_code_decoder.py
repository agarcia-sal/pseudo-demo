from typing import List

def fib4(n: int) -> int:
    results: List[int] = [0, 0, 2, 0]
    if n < 4:
        return results[n]
    for index in range(4, n + 1):
        new_value = results[-1] + results[-2] + results[-3] + results[-4]
        results.append(new_value)
        results.pop(0)
    return results[-1]