from typing import List

def all_prefixes(original_str: str) -> List[str]:
    def helper(i: int, accum: List[str]) -> List[str]:
        if i < 0:
            return accum
        else:
            return helper(i - 1, [original_str[:i + 1]] + accum)
    return helper(len(original_str) - 1, [])