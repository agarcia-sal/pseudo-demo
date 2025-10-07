from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_characters = [character for character in string_s if character not in string_c]
    result_string = ''.join(filtered_characters)
    is_palindrome = result_string == result_string[::-1]
    return result_string, is_palindrome