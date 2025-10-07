from typing import Sequence

def is_palindrome(text_string: Sequence[str]) -> bool:
    n = len(text_string)
    for i in range(n):
        if text_string[i] != text_string[n - 1 - i]:
            return False
    return True