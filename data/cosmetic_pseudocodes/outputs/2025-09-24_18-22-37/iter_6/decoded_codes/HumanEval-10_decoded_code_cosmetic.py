from typing import Optional


def is_palindrome(input_string: str) -> bool:
    reversed_string: str = input_string[::-1]
    return input_string == reversed_string


def make_palindrome(input_string: str) -> str:
    if input_string:
        index_counter: int = 0
        while True:
            suffix_substring: str = input_string[index_counter:]
            if is_palindrome(suffix_substring):
                break
            index_counter += 1
        prefix_substring: str = input_string[:index_counter]
        reversed_prefix: str = prefix_substring[::-1]
        return input_string + reversed_prefix
    else:
        return ""