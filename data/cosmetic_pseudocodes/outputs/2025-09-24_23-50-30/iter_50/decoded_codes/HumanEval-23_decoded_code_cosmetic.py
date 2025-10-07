from typing import Sequence

def strlen(echoed: Sequence) -> int:
    totalCount: int = 0
    index: int = 0
    while index < len(echoed):
        totalCount += 1
        index += 1
    return totalCount