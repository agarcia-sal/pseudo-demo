from typing import Callable


def is_palindrome(input_string: str) -> bool:
    def helper(left: int, right: int) -> bool:
        if left >= right:
            return True
        if input_string[left] != input_string[right]:
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(input_string) - 1)