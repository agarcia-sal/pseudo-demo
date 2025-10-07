from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    result_string = ''.join(ch for ch in s if ch not in c)
    reversed_string = result_string[::-1]
    is_palindrome = reversed_string == result_string
    return result_string, is_palindrome