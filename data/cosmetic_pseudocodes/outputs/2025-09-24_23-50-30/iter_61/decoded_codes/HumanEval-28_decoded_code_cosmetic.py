from typing import Callable


def concatenate(parameterOne: str) -> str:
    def helper(currentIndex: int, accumulator: str) -> str:
        if currentIndex >= len(parameterOne):
            return accumulator
        return helper(currentIndex + 1, accumulator + parameterOne[currentIndex])
    return helper(0, "")