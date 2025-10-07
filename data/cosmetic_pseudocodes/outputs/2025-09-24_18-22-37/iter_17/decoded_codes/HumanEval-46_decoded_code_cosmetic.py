from typing import List

def fib4(integer_n: int) -> int:
    alpha: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return alpha[integer_n]

    beta = 4
    while beta <= integer_n:
        gamma = alpha[3] + alpha[2] + alpha[1] + alpha[0]
        alpha.append(gamma)
        alpha.pop(0)
        beta += 1

    return alpha[3]