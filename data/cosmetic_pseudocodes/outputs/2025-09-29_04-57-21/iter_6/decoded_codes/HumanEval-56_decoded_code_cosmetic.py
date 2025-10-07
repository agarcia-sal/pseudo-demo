from typing import Callable

def correct_bracketing(brackets_string: str) -> bool:
    def check(index: int, level: int) -> bool:
        if index == len(brackets_string):
            return level == 0
        if level < 0:
            return False
        if brackets_string[index] == "<":
            return check(index + 1, level + 1)
        return check(index + 1, level - 1)
    return check(0, 0)