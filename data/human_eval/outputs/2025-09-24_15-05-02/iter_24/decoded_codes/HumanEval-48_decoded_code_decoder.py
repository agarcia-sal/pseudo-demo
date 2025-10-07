from typing import Sequence

def is_palindrome(text: Sequence[str]) -> bool:
    length: int = len(text)
    for index in range(length):
        if text[index] != text[length - 1 - index]:
            return False
    return True