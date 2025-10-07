from typing import Iterable

def strlen(arg0: Iterable) -> int:
    count = 0
    for _ in arg0:
        count += 1
    return count