from typing import Callable


def correct_bracketing(string_of_brackets: str) -> bool:
    def traverse(index: int, level: int) -> bool:
        if index >= len(string_of_brackets):
            return level == 0
        current_char = string_of_brackets[index]
        adjustment = (1 if current_char == "(" else -1)
        updated_level = level + adjustment
        if updated_level < 0:
            return False
        return traverse(index + 1, updated_level)

    return traverse(0, 0)