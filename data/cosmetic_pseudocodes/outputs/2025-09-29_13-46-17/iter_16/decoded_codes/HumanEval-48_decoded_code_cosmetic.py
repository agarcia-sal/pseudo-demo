from typing import Callable

def is_palindrome(text: str) -> bool:
    def ζ₁(κ_: int, ξ_: int) -> bool:
        if not (κ_ < ξ_):
            return True
        if text[κ_] != text[ξ_]:
            return False
        return ζ₁(κ_ + 1, ξ_ - 1)
    return ζ₁(0, len(text) - 1)