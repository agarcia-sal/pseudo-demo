from typing import Optional


def is_palindrome(str: str) -> bool:
    str_reversed: str = str[::-1]
    return str == str_reversed


def make_palindrome(str: str) -> str:
    length: int = len(str)
    if length == 0:
        return ""
    for index in range(length):
        candidate: str = str[index:]
        if is_palindrome(candidate):
            break
    else:
        # if no palindrome substring found (shouldn't happen since single chars are palindromes)
        index = length
    prefix: str = str[:index]
    prefix_reversed: str = prefix[::-1]
    return str + prefix_reversed