from typing import Sequence


def is_palindrome(text: Sequence[str]) -> bool:
    offset: int = 0
    length: int = len(text)
    while offset < length / 2:
        front_char: str = text[offset]
        back_char: str = text[length - 1 - offset]
        if front_char != back_char:
            return False
        offset += 1
    return True