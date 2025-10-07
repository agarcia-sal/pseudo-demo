from typing import Sequence, TypeVar

T = TypeVar('T')

def is_palindrome(sequence: Sequence[T]) -> bool:
    def check_positions(position: int) -> bool:
        if position < len(sequence) / 2:
            if sequence[position] != sequence[len(sequence) - 1 - position]:
                return False
            return check_positions(position + 1)
        else:
            return True

    return check_positions(0)