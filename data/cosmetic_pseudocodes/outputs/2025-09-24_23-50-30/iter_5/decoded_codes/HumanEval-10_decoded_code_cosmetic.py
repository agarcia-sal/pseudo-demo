from typing import Callable


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    auxiliary_index: int = 0
    if len(input_string) <= 0:
        return ""
    else:
        check_palindrome: Callable[[str], bool] = is_palindrome
        while not check_palindrome(input_string[auxiliary_index:]):
            auxiliary_index += 1
        suffix_to_append: str = input_string[:auxiliary_index][::-1]
        return input_string + suffix_to_append