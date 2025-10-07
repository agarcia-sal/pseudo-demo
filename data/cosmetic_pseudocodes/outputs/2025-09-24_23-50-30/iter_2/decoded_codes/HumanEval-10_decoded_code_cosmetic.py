from typing import Optional


def is_palindrome(input_string: str) -> bool:
    length = len(input_string)
    for idx in range(length // 2):
        if input_string[idx] != input_string[length - idx - 1]:
            return False
    return True


def make_palindrome(input_string: str) -> str:
    if not input_string:
        return ""

    def find_start(index: int) -> int:
        if index >= len(input_string):
            return len(input_string)
        if is_palindrome(input_string[index:]):
            return index
        return find_start(index + 1)

    start_palindrome = find_start(0)

    def recursive_reverse(s: str) -> str:
        if s == "":
            return ""
        return recursive_reverse(s[1:]) + s[0]

    return input_string + recursive_reverse(input_string[:start_palindrome])