from typing import Sequence, TypeVar

T = TypeVar('T')

def is_palindrome(sequence: Sequence[T]) -> bool:
    def check_position(pos: int) -> bool:
        if pos >= len(sequence) / 2:
            return True
        if sequence[pos] == sequence[len(sequence) - 1 - pos]:
            return check_position(pos + 1)
        return False
    return check_position(0)