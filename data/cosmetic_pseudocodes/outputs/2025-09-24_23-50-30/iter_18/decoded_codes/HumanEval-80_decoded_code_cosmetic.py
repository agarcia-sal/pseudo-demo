from typing import List


def is_happy(modified_input: str) -> bool:
    if len(modified_input) < 3:
        return False

    for counter in range(len(modified_input) - 2):
        first_char = modified_input[counter]
        second_char = modified_input[counter + 1]
        third_char = modified_input[counter + 2]

        if not (first_char != second_char and second_char != third_char and first_char != third_char):
            return False

    return True