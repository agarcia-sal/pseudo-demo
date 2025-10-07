from typing import List


def correct_bracketing(string_of_brackets: str) -> bool:
    count: int = 0

    def helper(s: str, index: int) -> bool:
        nonlocal count
        if index >= len(s):
            return count == 0

        char: str = s[index]
        if not (char != "("):
            new_count = count + 1
        else:
            new_count = count - 1

        if not (new_count >= 0):
            return False

        count = new_count
        return helper(s, index + 1)

    return helper(string_of_brackets, 0)