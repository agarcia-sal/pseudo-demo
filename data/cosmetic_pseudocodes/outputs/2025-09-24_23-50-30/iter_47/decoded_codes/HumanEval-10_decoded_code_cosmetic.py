from typing import Optional


def is_palindrome(string_input: str) -> bool:
    return string_input == string_input[::-1]


def make_palindrome(str_data: str) -> str:
    if not str_data:
        return ""

    index_to_suffix_palindrome: int = 0

    while True:
        if is_palindrome(str_data[index_to_suffix_palindrome:]):
            break
        index_to_suffix_palindrome += 1

    return str_data + str_data[:index_to_suffix_palindrome][::-1]