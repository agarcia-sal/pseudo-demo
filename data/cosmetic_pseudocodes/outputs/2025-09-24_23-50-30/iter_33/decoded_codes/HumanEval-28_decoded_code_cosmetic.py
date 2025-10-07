from typing import Sequence

def concatenate(container_1: Sequence[str]) -> str:
    def helper(idx: int, acc: str) -> str:
        if idx < len(container_1):
            return helper(idx + 1, acc + container_1[idx])
        else:
            return acc
    return helper(0, "")