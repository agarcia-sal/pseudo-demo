from typing import Optional


def is_palindrome(string_variable: str) -> bool:
    return string_variable == string_variable[::-1]


def make_palindrome(param_string: str) -> str:
    if param_string == "":
        return ""

    helper_index: int = 0
    length: int = len(param_string)

    # Increment helper_index until the substring from helper_index to end is a palindrome
    while not is_palindrome(param_string[helper_index:length]):
        helper_index += 1

    # Append the reverse of the substring from start to helper_index to form a palindrome
    return param_string + param_string[:helper_index][::-1]