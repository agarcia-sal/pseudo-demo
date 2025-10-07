from typing import Optional


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if input_string == "":
        return ""
    beginning_of_suffix: int = 0
    length: int = len(input_string)
    while beginning_of_suffix < length and not is_palindrome(input_string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    # beginning_of_suffix can be equal to length here if no palindrome found, but empty string is palindrome
    suffix_to_add: str = input_string[:beginning_of_suffix][::-1] if beginning_of_suffix <= length else ""
    return input_string + suffix_to_add