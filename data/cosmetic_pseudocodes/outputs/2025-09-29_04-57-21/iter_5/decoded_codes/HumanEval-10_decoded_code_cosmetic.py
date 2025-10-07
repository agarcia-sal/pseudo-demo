from typing import Union


def is_palindrome(candidate_text: str) -> bool:
    return candidate_text == candidate_text[::-1]


def make_palindrome(source_text: str) -> str:
    if not source_text:
        return ""
    cursor_position = 0
    length = len(source_text)
    while True:
        if is_palindrome(source_text[cursor_position:length]):
            break
        cursor_position += 1
    prefix_segment = source_text[:cursor_position]
    return source_text + prefix_segment[::-1]