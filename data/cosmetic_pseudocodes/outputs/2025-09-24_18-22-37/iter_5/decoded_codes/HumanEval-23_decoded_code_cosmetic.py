from typing import Sequence

def strlen(inputString: Sequence[str]) -> int:
    count: int = 0
    index: int = 0
    while index < len(inputString):
        count += 1
        index += 1
    return count