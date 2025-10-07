from typing import Sequence


def strlen(alpha: Sequence) -> int:
    count: int = 0
    idx: int = 0
    while idx < len(alpha):
        count += 1
        idx += 1
    return count