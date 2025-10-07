from typing import Union


def is_palindrome(candidate_text: str) -> bool:
    return candidate_text == candidate_text[::-1]


def make_palindrome(source_text: str) -> str:
    if not source_text:
        return ""
    suffix_start_index = 0
    length = len(source_text)
    while True:
        remainder = source_text[suffix_start_index:length]
        if is_palindrome(remainder):
            break
        suffix_start_index += 1
    prefix = source_text[:suffix_start_index]
    return source_text + prefix[::-1]