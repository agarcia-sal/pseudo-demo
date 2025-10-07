from typing import Callable

def is_palindrome(text: str) -> bool:
    length: int = len(text)

    def check(index: int) -> bool:
        if index >= length // 2:
            return True
        if text[index] != text[length - 1 - index]:
            return False
        return check(index + 1)

    if length == 0:
        return True
    return check(0)