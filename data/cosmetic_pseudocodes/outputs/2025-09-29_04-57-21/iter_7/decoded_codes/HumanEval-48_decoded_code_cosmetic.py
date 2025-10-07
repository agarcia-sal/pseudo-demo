from typing import Sequence

def is_palindrome(sequence: Sequence[str]) -> bool:
    position: int = 0
    length: int = len(sequence)
    while position < length:
        front_char: str = sequence[position]
        back_char: str = sequence[length - 1 - position]
        if front_char != back_char:
            return False
        position += 1
    return True