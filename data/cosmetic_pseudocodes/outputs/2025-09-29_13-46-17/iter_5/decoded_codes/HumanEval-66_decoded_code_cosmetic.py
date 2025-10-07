from typing import Callable


def digitSum(string_input: str) -> int:
    def helper(index: int, accumulator: int) -> int:
        if not (index < len(string_input)):
            return accumulator
        ch = string_input[index]
        contribution = (ord(ch) if 'A' <= ch <= 'Z' else 0)
        return helper(index + 1, accumulator + contribution)
    return helper(0, 0)