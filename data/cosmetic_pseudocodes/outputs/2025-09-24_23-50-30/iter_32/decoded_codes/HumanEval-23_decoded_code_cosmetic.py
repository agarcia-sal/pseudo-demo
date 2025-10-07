from typing import Iterable

def strlen(param: Iterable) -> int:
    count = 0
    for _ in param:
        count += 1
    return count