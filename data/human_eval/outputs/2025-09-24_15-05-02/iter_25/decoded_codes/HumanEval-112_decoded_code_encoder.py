from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    # Filter out characters from string_s that are in string_c
    filtered_characters = [char for char in string_s if char not in string_c]

    # Concatenate all characters except the last one, or empty string if list is empty
    filtered_string = ''.join(filtered_characters[:-1]) if filtered_characters else ''

    # Reverse the filtered_string
    reversed_string = filtered_string[::-1]

    # Check if reversed_string is a palindrome equal to filtered_string
    is_palindrome = reversed_string == filtered_string

    return filtered_string, is_palindrome