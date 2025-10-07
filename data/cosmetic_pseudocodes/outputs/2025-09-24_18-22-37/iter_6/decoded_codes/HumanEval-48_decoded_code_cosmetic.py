from typing import Sequence


def is_palindrome(sequence: Sequence[str]) -> bool:
    pointer: int = 0
    length: int = len(sequence)
    while pointer < length:
        left_char: str = sequence[pointer]
        right_pos: int = length - 1 - pointer
        right_char: str = sequence[right_pos]
        if left_char == right_char:
            pointer += 1
        else:
            return False
    return True