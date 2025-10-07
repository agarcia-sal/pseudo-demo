from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = [ch for ch in string_s if ch not in string_c]
    processed_string = ''.join(filtered_chars)

    left, right = 0, len(processed_string) - 1
    palindrome_flag = True
    while left < right and palindrome_flag:
        if processed_string[left] != processed_string[right]:
            palindrome_flag = False
        left += 1
        right -= 1

    return processed_string, palindrome_flag