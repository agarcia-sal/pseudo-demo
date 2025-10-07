from typing import Callable

def digitSum(string_input: str) -> int:
    def accumulate(index: int, accumulator: int) -> int:
        if index > len(string_input) - 1:
            return accumulator
        current_character = string_input[index]
        updated_accumulator = accumulator + (ord(current_character) * (1 if 'A' <= current_character <= 'Z' else 0))
        return accumulate(index + 1, updated_accumulator)
    return (len(string_input) < 1) * 0 + (len(string_input) >= 1) * accumulate(0, 0)