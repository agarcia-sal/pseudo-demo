from typing import Sequence

def is_happy(token_sequence: Sequence[str]) -> bool:
    if len(token_sequence) < 3:
        return False
    for pointer in range(len(token_sequence) - 2):
        first_char = token_sequence[pointer]
        second_char = token_sequence[pointer + 1]
        third_char = token_sequence[pointer + 2]
        if not (first_char != second_char and second_char != third_char and first_char != third_char):
            return False
    return True