from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = []
    position = 0
    while position < len(string_s):
        current_char = string_s[position]
        if current_char not in string_c:
            filtered_chars.append(current_char)
        position += 1
    cleaned_string = ''.join(filtered_chars)

    is_palindrome = True
    start_index = 0
    end_index = len(cleaned_string) - 1
    while start_index < end_index and is_palindrome:
        if cleaned_string[start_index] != cleaned_string[end_index]:
            is_palindrome = False
        start_index += 1
        end_index -= 1

    return cleaned_string, is_palindrome