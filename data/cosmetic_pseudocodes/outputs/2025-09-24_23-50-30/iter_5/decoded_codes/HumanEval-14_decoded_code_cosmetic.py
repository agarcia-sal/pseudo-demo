from typing import List

def all_prefixes(alpha: str) -> List[str]:
    def helper(acc: List[str], pos: int) -> List[str]:
        if pos == len(alpha):
            return acc
        return helper(acc + [alpha[:pos + 1]], pos + 1)
    return helper([], 0)