from typing import Callable


def is_palindrome(input_string: str) -> bool:
    def recurse_check(text: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return recurse_check(text, left + 1, right - 1)
    return recurse_check(input_string, 0, len(input_string) - 1)


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""
    search_start = 0
    length = len(input_string)
    while True:
        sub_check = input_string[search_start:length]
        if is_palindrome(sub_check):
            break
        search_start += 1
    return input_string + input_string[:search_start][::-1]