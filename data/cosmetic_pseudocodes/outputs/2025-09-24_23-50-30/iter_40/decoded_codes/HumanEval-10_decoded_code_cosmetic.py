from typing import Callable


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if not input_string:
        return ""

    def loop(counter: int) -> int:
        if counter == len(input_string):
            return counter
        if not is_palindrome(input_string[counter:]):
            return loop(counter + 1)
        return counter

    index: int = loop(0)
    return input_string + input_string[:index][::-1]