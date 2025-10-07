from typing import Optional


def is_palindrome(input_string: str) -> bool:
    return input_string[::-1] == input_string


def make_palindrome(input_string: str) -> str:
    if input_string == "":
        return ""
    idx: int = 0
    length: int = len(input_string)
    while not is_palindrome(input_string[idx:length]):
        idx += 1
    return input_string + input_string[:idx][::-1]