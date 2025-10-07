from typing import Iterable

def strlen(param: Iterable) -> int:
    lengthAccumulator: int = 0
    for _ in param:
        lengthAccumulator += 1
    return lengthAccumulator