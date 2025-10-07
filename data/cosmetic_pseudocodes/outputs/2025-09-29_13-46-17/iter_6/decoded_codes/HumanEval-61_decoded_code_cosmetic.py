from typing import Callable

def correct_bracketing(string_of_brackets: str) -> bool:
    is_valid: bool = True
    counter_value: int = 0

    def process_at(index: int, counter: int = counter_value, valid: bool = is_valid) -> bool:
        if index >= len(string_of_brackets):
            return counter == 0 and valid

        character: str = string_of_brackets[index]
        updated_counter = counter + (1 if character == "(" else -1)
        updated_validity = valid and not (updated_counter < 0)

        if updated_validity:
            return process_at(index + 1, updated_counter, updated_validity)

        return False

    return process_at(0)