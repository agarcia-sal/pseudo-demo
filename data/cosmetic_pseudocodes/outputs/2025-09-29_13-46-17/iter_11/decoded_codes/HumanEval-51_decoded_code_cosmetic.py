from typing import Callable

def remove_vowels(text: str) -> str:
    def remove_vowels_(s: str) -> str:
        if not s:
            return ""
        head, tail = s[0], s[1:]
        lower_head = head.lower()
        if lower_head not in {"a", "e", "i", "o", "u"}:
            return head + remove_vowels_(tail)
        else:
            return remove_vowels_(tail)
    return remove_vowels_(text)