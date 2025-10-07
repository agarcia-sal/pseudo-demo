from typing import Sequence, Union

def is_palindrome(text: Union[str, Sequence[str]]) -> bool:
    start: int = 0
    end: int = len(text) - 1
    while start < end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    return True