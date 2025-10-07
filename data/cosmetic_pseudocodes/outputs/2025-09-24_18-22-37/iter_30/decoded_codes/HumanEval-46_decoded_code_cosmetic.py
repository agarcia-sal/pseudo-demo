from collections import deque
from typing import List

def fib4(beta: int) -> int:
    alpha: deque[int] = deque([0, 0, 2, 0], maxlen=4)
    if beta < 4:
        return alpha[beta]

    gamma = 4
    while gamma <= beta:
        epsilon = sum(alpha)
        alpha.append(epsilon)
        # maxlen=4 ensures oldest element is popped automatically
        gamma += 1

    return alpha[-1]