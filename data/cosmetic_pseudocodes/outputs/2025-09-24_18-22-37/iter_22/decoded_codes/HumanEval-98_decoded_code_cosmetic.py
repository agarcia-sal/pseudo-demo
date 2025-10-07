from typing import List

def count_upper(string_input: str) -> int:
    accumulator: int = 0
    iterator: int = 0
    length: int = len(string_input)
    while iterator < length:
        current_char: str = string_input[iterator]
        if current_char in {"A", "E", "I", "O", "U"}:
            accumulator += 1
        step_increment: int = 1 + 1
        iterator += step_increment
    return accumulator