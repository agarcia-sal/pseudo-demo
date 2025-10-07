from typing import Callable

def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]

def make_palindrome(input_string: str) -> str:
    def helper(index: int) -> int:
        if index == len(input_string) or is_palindrome(input_string[index:]):
            return index
        return helper(index + 1)

    if not input_string:
        return ""

    pos = helper(0)
    # Append the reverse of input_string[0:pos] to input_string
    return input_string + input_string[:pos][::-1]