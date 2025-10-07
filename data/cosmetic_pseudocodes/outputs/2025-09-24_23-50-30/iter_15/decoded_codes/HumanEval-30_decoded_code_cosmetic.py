from collections import deque
from typing import Iterable, Deque

def get_positive(beta: Iterable[int]) -> Deque[int]:
    gamma: Deque[int] = deque()
    for delta in beta:
        if delta <= 0:
            continue
        gamma.append(delta)
    return gamma