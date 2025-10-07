from typing import Iterable

def strlen(text: Iterable[str]) -> int:
    count: int = 0
    for _ in text:
        count += 1
    return count