from typing import Literal


def is_palindrome(input_string: str) -> bool:
    return helper_check(input_string, len(input_string) - 1, 0)


def helper_check(s: str, endIdx: int, startIdx: int) -> bool:
    if startIdx >= endIdx:
        return True
    if s[startIdx] != s[endIdx]:
        return False
    return helper_check(s, endIdx - 1, startIdx + 1)


def make_palindrome(input_string: str) -> str:
    if not input_string:
        return ""
    idx = 0
    condition: bool = False

    while not condition:
        tail_substring = input_string[idx:]
        condition = is_palindrome(tail_substring)
        if not condition:
            idx += 1

    return input_string + input_string[:idx][::-1]