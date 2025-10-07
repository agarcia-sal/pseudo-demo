from typing import AnyStr


def is_palindrome(input_string: str) -> bool:
    temp_string = ""
    for idx in range(len(input_string) - 1, -1, -1):
        temp_string += input_string[idx]
    return input_string == temp_string


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    start_index = 0
    while True:
        check_substring = input_string[start_index:]
        if is_palindrome(check_substring):
            break
        start_index += 1

    prefix = ""
    for i in range(start_index - 1, -1, -1):
        prefix += input_string[i]

    return input_string + prefix