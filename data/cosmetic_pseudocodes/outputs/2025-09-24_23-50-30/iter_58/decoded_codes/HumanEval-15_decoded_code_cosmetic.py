from functools import reduce
from typing import List

def string_sequence(alpha: int) -> str:
    beta: List[str] = []
    gamma: int = 0
    while gamma <= alpha:
        beta.append(str(gamma))
        gamma += 1  # increment by 1 (1 - 0)
    return reduce(lambda x, y: x + " " + y, beta)