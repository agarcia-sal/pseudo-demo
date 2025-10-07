from typing import Optional


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    idx: int = 0
    if len(input_string) == 0:
        return ""
    while True:
        segment = input_string[idx:]
        if is_palindrome(segment):
            break
        idx += 1
    return input_string + input_string[:idx][::-1]