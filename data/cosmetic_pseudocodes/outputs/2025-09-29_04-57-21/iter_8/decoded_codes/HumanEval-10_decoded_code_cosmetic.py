from typing import Optional

def is_palindrome(text: str) -> bool:
    return text == text[::-1]

def make_palindrome(text: str) -> str:
    if len(text) == 0:
        return ""
    suffix_start = 0
    while True:
        if is_palindrome(text[suffix_start:]):
            break
        suffix_start += 1
    return text + text[:suffix_start][::-1]