from typing import Callable

def correct_bracketing(brackets_string: str) -> bool:
    def recursive_check(index: int, depth: int) -> bool:
        if index >= len(brackets_string):
            return depth == 0
        current_char = brackets_string[index]
        new_depth = depth + 1 if current_char == "<" else depth - 1
        if new_depth < 0:
            return False
        return recursive_check(index + 1, new_depth)
    return recursive_check(0, 0)