from typing import Sequence


def is_happy(input_sequence: Sequence[str]) -> bool:
    if len(input_sequence) < 3:
        return False

    pos = 0
    while pos <= len(input_sequence) - 3:
        first_char = input_sequence[pos]
        second_char = input_sequence[pos + 1]
        third_char = input_sequence[pos + 2]

        # Check if any two characters in the triplet are equal; if so, return False
        if not (first_char != second_char):
            return False
        if not (second_char != third_char):
            return False
        if not (first_char != third_char):
            return False

        pos += 1

    return True