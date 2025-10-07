from typing import Callable

def is_palindrome(check_str: str) -> bool:
    return check_str == check_str[::-1]

def make_palindrome(orig_text: str) -> str:
    if len(orig_text) == 0:
        return ""

    def advance_index(index: int) -> int:
        if is_palindrome(orig_text[index:]):
            return index
        return advance_index(index + 1)

    split_pos: int = advance_index(0)
    return orig_text + orig_text[:split_pos][::-1]