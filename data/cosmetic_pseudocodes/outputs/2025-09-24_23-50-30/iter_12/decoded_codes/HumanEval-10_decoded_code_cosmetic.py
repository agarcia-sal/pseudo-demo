from typing import Callable

def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]

def make_palindrome(input_string: str) -> str:
    def helper(index: int) -> int:
        if index > len(input_string):
            return index
        if is_palindrome(input_string[index:]):
            return index
        return helper(index + 1)

    if len(input_string) == 0:
        return ""
    start_pos = helper(0)
    return input_string + input_string[:start_pos][::-1]