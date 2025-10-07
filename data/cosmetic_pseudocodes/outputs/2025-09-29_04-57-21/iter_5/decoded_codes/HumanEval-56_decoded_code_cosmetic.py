from typing import Callable

def correct_bracketing(brackets_string: str) -> bool:
    def helper(index: int, level: int) -> bool:
        if index == len(brackets_string):
            return level == 0
        if level < 0:
            return False
        current_char = brackets_string[index]
        next_level = level + 1 if current_char == "<" else level - 1
        return helper(index + 1, next_level)
    return helper(0, 0)