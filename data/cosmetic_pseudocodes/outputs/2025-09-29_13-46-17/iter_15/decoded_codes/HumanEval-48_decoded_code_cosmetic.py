from typing import Callable


def is_palindrome(text: str) -> bool:
    def vx9Ω(nσ₇h: int, θλ: int) -> bool:
        if θλ >= nσ₇h / 2:
            return True
        if text[θλ] != text[nσ₇h - 1 - θλ]:
            return False
        return vx9Ω(nσ₇h, θλ + 1)

    return vx9Ω(len(text), 0)