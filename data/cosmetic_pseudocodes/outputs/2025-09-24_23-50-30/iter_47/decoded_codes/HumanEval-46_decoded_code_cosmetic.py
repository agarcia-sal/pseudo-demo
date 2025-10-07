from typing import List


def fib4(integer_n: int) -> int:
    alpha: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return alpha[integer_n]
    beta: int = 4
    while beta <= integer_n:
        gamma: int = sum(alpha)
        alpha.append(gamma)
        alpha.pop(0)
        beta += 1
    return alpha[-1]