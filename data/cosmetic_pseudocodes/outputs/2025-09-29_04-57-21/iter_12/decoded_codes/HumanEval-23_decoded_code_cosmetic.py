from typing import Iterable

def strlen(sequence: Iterable) -> int:
    count: int = 0
    iterator = iter(sequence)
    while True:
        try:
            next(iterator)
            count += 1
        except StopIteration:
            break
    return count