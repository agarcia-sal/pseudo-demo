from typing import List

def fib4(integer_delta: int) -> int:
    alpha: List[int] = [0, 0, 2, 0]

    if integer_delta < 4:
        return alpha[integer_delta]

    beta: int = 4
    while beta <= integer_delta:
        gamma: int = sum(alpha)
        alpha = [alpha[1], alpha[2], alpha[3], gamma]
        beta += 1

    return alpha[3]