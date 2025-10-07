from typing import Callable

def correct_bracketing(brackets_string: str) -> bool:
    def inner_check(current_idx: int, depth_accum: int) -> bool:
        if current_idx >= len(brackets_string):
            return depth_accum == 0
        current_char = brackets_string[current_idx]
        updated_depth = depth_accum + (1 if current_char == "<" else -1)
        if updated_depth < 0:
            return False
        return inner_check(current_idx + 1, updated_depth)

    return inner_check(0, 0)