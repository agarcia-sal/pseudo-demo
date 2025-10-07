from typing import List

def all_prefixes(q: str) -> List[str]:
    A: List[str] = []

    def recur(i: int) -> None:
        if i < 0:
            return
        else:
            recur(i - 1)
            v = q[:i + 1]
            A.append(v)

    recur(len(q) - 1)
    return A