from typing import Literal


def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False
    limit = len(string_input) - 3
    for counter in range(limit + 1):
        first_char = string_input[counter]
        second_char = string_input[counter + 1]
        third_char = string_input[counter + 2]
        # Return False if any two characters in the triplet are equal
        if not (first_char != second_char and second_char != third_char and first_char != third_char):
            return False
    return True