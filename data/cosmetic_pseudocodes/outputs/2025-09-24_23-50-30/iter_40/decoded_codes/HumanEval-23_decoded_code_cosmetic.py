from typing import Sequence

def strlen(anyStr: Sequence) -> int:
    acc: int = 0
    while acc != len(anyStr):
        acc += 1
    return acc