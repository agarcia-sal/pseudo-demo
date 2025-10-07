from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_string = ''.join(character for character in string_s if character not in string_c)
    is_palindrome = filtered_string == filtered_string[::-1]
    return filtered_string, is_palindrome