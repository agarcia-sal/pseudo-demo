from typing import List


def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return window[integer_n]

    for _ in range(4, integer_n + 1):
        total = sum(window[-j] for j in range(1, 5))
        window.pop(0)
        window.append(total)

    return window[4 - 1]