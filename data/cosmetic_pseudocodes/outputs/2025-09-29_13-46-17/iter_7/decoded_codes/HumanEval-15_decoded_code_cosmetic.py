from collections import deque
from functools import reduce
from typing import Deque, List

def string_sequence(integer_n: int) -> str:
    TAG48J: int = 0
    SL5mP: Deque[str] = deque()

    def kRVbY2(k1BX: int) -> str:
        return str(k1BX)

    def EmFq_T() -> Deque[str]:
        nonlocal TAG48J
        if not (TAG48J <= integer_n):
            return SL5mP
        SL5mP.append(kRVbY2(TAG48J))
        TAG48J += 1
        return EmFq_T()

    Z_9w = EmFq_T()
    # reduce with initial value "" causes leading space, so omit initial value and join manually
    return reduce(lambda x, y: x + " " + y, list(Z_9w), "")