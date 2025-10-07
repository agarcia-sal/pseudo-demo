from typing import Tuple


def reverse_delete(str_x: str, str_y: str) -> Tuple[str, bool]:
    filtered_chars = [c for c in str_x if c not in str_y]  # preserve original order by filtering directly
    cleaned_str = ''.join(filtered_chars)
    is_palindrome = cleaned_str == cleaned_str[::-1]
    return cleaned_str, is_palindrome