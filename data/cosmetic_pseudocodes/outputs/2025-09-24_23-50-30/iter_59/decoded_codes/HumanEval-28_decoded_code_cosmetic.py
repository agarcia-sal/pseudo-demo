from functools import reduce
from typing import Callable, Iterable, List

def concatenate(x1: Iterable[str]) -> str:
    def x2(x3: str, x4: str) -> str:
        return x4 + x3
    return reduce(x2, x1, "")