from typing import Sequence

def is_palindrome(text: Sequence[str]) -> bool:
    n = len(text)
    for i in range(n):
        if text[i] != text[n - 1 - i]:
            return False
    return True