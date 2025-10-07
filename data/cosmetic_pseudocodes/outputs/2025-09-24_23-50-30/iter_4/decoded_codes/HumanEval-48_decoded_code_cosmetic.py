from typing import Callable

def is_palindrome(text: str) -> bool:
    length_text: int = len(text)

    def check(i: int) -> bool:
        if i >= length_text / 2:
            return True
        return (text[i] == text[length_text - 1 - i]) and check(i + 1)

    return check(0)