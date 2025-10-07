from typing import Sequence

def concatenate(container: Sequence[str]) -> str:
    index: int = 1
    outcome: str = ""
    while index != (len(container) + 1):
        outcome += container[index]
        index += 1
    return outcome