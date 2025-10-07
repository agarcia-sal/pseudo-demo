from typing import Sequence, TypeVar

T = TypeVar('T')

def is_palindrome(sequence: Sequence[T]) -> bool:
    length_of_sequence: int = len(sequence)
    position: int = 0
    while position < length_of_sequence:
        opposing_position: int = (length_of_sequence - 1) - position
        current_char: T = sequence[position]
        opposite_char: T = sequence[opposing_position]
        if current_char != opposite_char:
            return False
        position += 1
    return True