from typing import Tuple


def reverse_delete(string_p: str, string_q: str) -> Tuple[str, bool]:
    buffer_r = ''.join(ch for ch in string_p if ch not in string_q)

    def is_palindrome_recursive(start_x: int, end_y: int) -> bool:
        if start_x >= end_y:
            return True
        return buffer_r[start_x] == buffer_r[end_y] and is_palindrome_recursive(start_x + 1, end_y - 1)

    return buffer_r, is_palindrome_recursive(0, len(buffer_r) - 1)