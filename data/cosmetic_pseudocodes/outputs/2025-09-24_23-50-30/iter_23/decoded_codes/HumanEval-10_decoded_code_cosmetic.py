from typing import Callable

def is_palindrome(variant_alpha: str) -> bool:
    return variant_alpha == variant_alpha[::-1]

def make_palindrome(variant_alpha: str) -> str:
    def find_start(offset: int) -> int:
        if offset == len(variant_alpha) or is_palindrome(variant_alpha[offset:]):
            return offset
        else:
            return find_start(offset + 1)

    if len(variant_alpha) == 0:
        return ""

    pivot: int = find_start(0)
    return variant_alpha + variant_alpha[:pivot][::-1]