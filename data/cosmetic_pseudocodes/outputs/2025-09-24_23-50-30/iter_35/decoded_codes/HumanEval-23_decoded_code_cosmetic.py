from typing import Sequence

def strlen(data: Sequence) -> int:
    count: int = 0
    while count < len(data):
        count += 1
    return count