from typing import Callable

def digitSum(string_input: str) -> int:
    def calculateSum(index: int, accumulator: int) -> int:
        if index >= len(string_input):
            return accumulator
        current_char = string_input[index]
        if not ('A' <= current_char <= 'Z'):
            return calculateSum(index + 1, accumulator)
        return calculateSum(index + 1, accumulator + ord(current_char))

    return 0 if string_input == "" else calculateSum(0, 0)