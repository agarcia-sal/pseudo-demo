from typing import Tuple

def reverse_delete(string_x: str, string_y: str) -> Tuple[str, bool]:
    filtered_str = ''.join(char for char in string_x if char not in string_y)
    reversed_str = filtered_str[::-1]  # Reverse the filtered string using slicing
    is_palindrome = reversed_str == filtered_str
    return filtered_str, is_palindrome