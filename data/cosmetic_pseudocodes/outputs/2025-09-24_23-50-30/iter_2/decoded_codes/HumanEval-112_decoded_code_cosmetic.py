from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars: list[str] = []
    # Iterate over indices from len(string_s) down to 1 (1-based indexing in pseudocode)
    for i in range(len(string_s), 0, -1):
        char = string_s[i - 1]  # convert to 0-based index
        if char in string_c:
            continue
        filtered_chars.insert(0, char)  # insert at start

    new_s = ''.join(filtered_chars)
    is_palindrome = new_s == new_s[::-1]
    return new_s, is_palindrome