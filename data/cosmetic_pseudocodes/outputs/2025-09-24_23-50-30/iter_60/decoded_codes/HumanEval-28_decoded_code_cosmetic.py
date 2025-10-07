from typing import Sequence

def concatenate(q: Sequence[str]) -> str:
    if len(q) > 1:
        return q[0] + concatenate(q[1:])
    if len(q) == 1:
        return q[0]
    return ""