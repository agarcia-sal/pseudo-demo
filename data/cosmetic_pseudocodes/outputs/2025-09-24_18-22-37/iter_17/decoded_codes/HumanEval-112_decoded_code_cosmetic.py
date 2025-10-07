from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    buffer: str = ""
    pos: int = 0
    while pos < len(string_s):
        current_char: str = string_s[pos]
        if current_char not in string_c:
            buffer += current_char
        pos += 1

    reversed_buffer: str = ""
    idx: int = len(buffer) - 1
    while idx >= 0:
        reversed_buffer += buffer[idx]
        idx -= 1

    is_palindrome: bool = (reversed_buffer == buffer)
    return buffer, is_palindrome