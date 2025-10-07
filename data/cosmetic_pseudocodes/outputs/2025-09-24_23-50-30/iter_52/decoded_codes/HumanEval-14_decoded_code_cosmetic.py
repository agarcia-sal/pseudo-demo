from typing import List

def all_prefixes(a_string: str) -> List[str]:
    def helper(pos: int, acc: List[str]) -> List[str]:
        if pos == len(a_string):
            return acc
        return helper(pos + 1, acc + [a_string[:pos + 1]])
    return helper(0, [])