from typing import Optional


def correct_bracketing(string_of_brackets: str) -> bool:
    def helper(s: str, index: int, depth: int) -> bool:
        if index == len(s):
            return depth == 0
        if s[index] == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
        return helper(s, index + 1, depth)

    return helper(string_of_brackets, 0, 0)