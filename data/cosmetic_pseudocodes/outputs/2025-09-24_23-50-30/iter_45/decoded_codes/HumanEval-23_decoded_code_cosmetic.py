from typing import Sequence

def strlen(chars: Sequence) -> int:
    count: int = 0
    while count < len(chars):
        count += 1
    return count