from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = [ch for ch in string_s if ch not in string_c]
    result_string = ''.join(filtered_chars)
    is_palindrome_flag = result_string == result_string[::-1]
    return result_string, is_palindrome_flag