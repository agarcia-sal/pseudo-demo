from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    list_temp: list[str] = []
    idx: int = 0
    while idx < len(string_s):
        ch: str = string_s[idx]
        flag_contains: bool = False
        idx_c: int = 0
        while idx_c < len(string_c):
            if ch == string_c[idx_c]:
                flag_contains = True
                break
            idx_c += 1
        if not flag_contains:
            list_temp.append(ch)
        idx += 1

    filtered_str: str = ''
    pos: int = 0
    while pos < len(list_temp):
        filtered_str += list_temp[pos]
        pos += 1

    rev_str: str = ''
    rev_pos: int = len(filtered_str) - 1
    while rev_pos >= 0:
        rev_str += filtered_str[rev_pos]
        rev_pos -= 1

    is_palindrome: bool = (rev_str == filtered_str)

    return filtered_str, is_palindrome