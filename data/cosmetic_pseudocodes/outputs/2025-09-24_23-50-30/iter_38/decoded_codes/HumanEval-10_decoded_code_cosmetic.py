from typing import Optional


def is_palindrome(a_string: str) -> bool:
    return a_string == a_string[::-1]


def make_palindrome(a_string: str) -> str:
    if a_string == "":
        return ""

    index_start_pal_suffix: int = 0
    length = len(a_string)

    # Find the start index of the longest palindromic suffix
    while not is_palindrome(a_string[index_start_pal_suffix:length]):
        index_start_pal_suffix += 1

    # Append the reverse of the prefix up to that index to form a palindrome
    return a_string + a_string[:index_start_pal_suffix][::-1]