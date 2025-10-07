from typing import Callable


def is_happy(string_input: str) -> bool:
    total_length: int = len(string_input)
    if total_length < 3:
        return False

    def check_triplet(position: int) -> bool:
        if position > total_length - 3:
            return True
        first_char: str = string_input[position]
        second_char: str = string_input[position + 1]
        third_char: str = string_input[position + 2]

        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False

        return check_triplet(position + 1)

    return check_triplet(0)