from typing import Callable


def correct_bracketing(brackets_string: str) -> bool:
    def check(index: int, nestedLevel: int) -> bool:
        if index >= len(brackets_string):
            return nestedLevel == 0

        currentChar = brackets_string[index]
        nextLevel = nestedLevel + 1 if currentChar == "<" else nestedLevel - 1

        if nextLevel < 0:
            return False

        return check(index + 1, nextLevel)

    return check(0, 0)