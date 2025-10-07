from typing import Sequence

def strlen(text: Sequence[str]) -> int:
    count: int = 0
    for _ in text:
        count += 1
    return count