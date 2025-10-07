from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars: list[str] = []
    idx_i: int = 0
    while idx_i < len(string_s):
        current_char: str = string_s[idx_i]
        if current_char not in string_c:
            filtered_chars.append(current_char)
        idx_i += 1
    result_str: str = "".join(filtered_chars)
    rev_str: str = ""
    pos_j: int = len(result_str) - 1
    while pos_j >= 0:
        rev_str += result_str[pos_j]
        pos_j -= 1
    palindrome_check: bool = rev_str == result_str
    return result_str, palindrome_check