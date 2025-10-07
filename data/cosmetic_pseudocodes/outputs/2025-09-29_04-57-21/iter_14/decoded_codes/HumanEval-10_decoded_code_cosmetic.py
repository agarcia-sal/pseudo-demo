from typing import Union


def is_palindrome(query_string: str) -> bool:
    return query_string == query_string[::-1]


def make_palindrome(source_string: str) -> str:
    if source_string == "":
        return ""

    pal_suffix_start = 0
    length = len(source_string)
    # Find the smallest suffix starting at pal_suffix_start that forms a palindrome
    while not is_palindrome(source_string[pal_suffix_start:length]):
        pal_suffix_start += 1

    return source_string + source_string[:pal_suffix_start][::-1]