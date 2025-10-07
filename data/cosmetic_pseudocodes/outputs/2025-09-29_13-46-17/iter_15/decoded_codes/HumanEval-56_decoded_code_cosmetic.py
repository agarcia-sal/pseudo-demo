from typing import Callable


def correct_bracketing(brackets_string: str) -> bool:
    def helper(depth: int, index: int) -> bool:
        if index >= len(brackets_string):
            return depth == 0
        current_char = brackets_string[index]
        delta = 1 if current_char == "<" else -1
        new_depth = depth + delta
        if new_depth < 0:
            return False
        return helper(new_depth, index + 1)

    return helper(0, 0)