from typing import Iterable, Set

def same_chars(alpha: Iterable[str], beta: Iterable[str]) -> bool:
    def helper(chars: Iterable[str]) -> Set[str]:
        acc: Set[str] = set()
        pos: int = 0
        chars_list = list(chars)
        while pos < len(chars_list):
            acc.add(chars_list[pos])
            pos += 1
        return acc

    return helper(alpha) == helper(beta)