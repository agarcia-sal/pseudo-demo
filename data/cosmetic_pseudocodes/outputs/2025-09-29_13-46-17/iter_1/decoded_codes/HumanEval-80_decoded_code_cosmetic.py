from typing import Literal


def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False
    for i in range(len(string_input) - 2):
        first_char: str = string_input[i]
        second_char: str = string_input[i + 1]
        third_char: str = string_input[i + 2]
        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False
    return True