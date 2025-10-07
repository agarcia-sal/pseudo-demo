from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = [char for char in string_s if char not in string_c]
    result_string = ''.join(filtered_chars)
    is_palindrome = (result_string == result_string[::-1])
    return result_string, is_palindrome