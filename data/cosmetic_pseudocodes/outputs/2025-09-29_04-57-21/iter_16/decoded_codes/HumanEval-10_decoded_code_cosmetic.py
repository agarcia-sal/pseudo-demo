from typing import NoReturn


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if input_string == "":
        return ""

    palindromic_start_index: int = 0

    while True:
        substr_check = input_string[palindromic_start_index:]
        if is_palindrome(substr_check):
            break
        palindromic_start_index += 1

    prefix = input_string[:palindromic_start_index]
    return input_string + prefix[::-1]