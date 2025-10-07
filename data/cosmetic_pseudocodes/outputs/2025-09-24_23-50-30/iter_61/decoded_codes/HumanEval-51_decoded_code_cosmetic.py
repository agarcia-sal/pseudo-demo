from typing import List


def remove_vowels(p: List[str]) -> List[str]:
    if not p:
        return []
    x, *lst = p
    if x.lower() in {"a", "e", "i", "o", "u"}:
        return remove_vowels(lst)
    return [x] + remove_vowels(lst)