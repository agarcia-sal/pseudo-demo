from typing import Sequence, TypeVar

T = TypeVar('T')

def is_palindrome(sequence: Sequence[T]) -> bool:
    def recursiveCheck(position: int) -> bool:
        if position >= len(sequence) / 2:
            return True
        if sequence[position] != sequence[len(sequence) - 1 - position]:
            return False
        return recursiveCheck(position + 1)

    return recursiveCheck(0)