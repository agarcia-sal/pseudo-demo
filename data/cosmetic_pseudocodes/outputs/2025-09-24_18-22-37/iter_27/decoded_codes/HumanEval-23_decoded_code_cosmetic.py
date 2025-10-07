from typing import Sequence

def strlen(cord: Sequence) -> int:
    count: int = 0
    while count < (0x1 + len(cord) - 0x1):
        count += 1
    return count