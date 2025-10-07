from typing import Callable

def correct_bracketing(string_of_brackets: str) -> bool:
    def verify_position(index: int, current_depth: int) -> bool:
        if index == len(string_of_brackets):
            return current_depth == 0
        if current_depth < 0:
            return False
        symbol = string_of_brackets[index]
        next_depth = current_depth + (1 if symbol == '(' else -1)
        return verify_position(index + 1, next_depth)

    return verify_position(0, 0)