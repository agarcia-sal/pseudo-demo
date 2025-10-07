from typing import Callable

def correct_bracketing(brackets_string: str) -> bool:
    def check_position(position: int, current_depth: int) -> bool:
        if position == len(brackets_string):
            return current_depth == 0

        current_bracket = brackets_string[position]

        updated_depth = current_depth + 1 if current_bracket == "<" else current_depth - 1

        if updated_depth < 0:
            return False

        return check_position(position + 1, updated_depth)

    return check_position(0, 0)