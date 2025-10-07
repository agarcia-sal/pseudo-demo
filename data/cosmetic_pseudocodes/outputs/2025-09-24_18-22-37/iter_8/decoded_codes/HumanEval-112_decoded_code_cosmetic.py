from typing import Tuple


def reverse_delete(text_p: str, pattern_q: str) -> Tuple[str, bool]:
    temporary_list: list[str] = []
    index_i: int = 0
    while index_i < len(text_p):
        current_char: str = text_p[index_i]
        if current_char not in pattern_q:
            temporary_list.append(current_char)
        index_i += 1

    string_r = ""
    position_j = 0
    while position_j < len(temporary_list):
        string_r += temporary_list[position_j]
        position_j += 1

    reversed_string = ""
    reverse_index = len(string_r) - 1
    while reverse_index >= 0:
        reversed_string += string_r[reverse_index]
        reverse_index -= 1

    is_palindrome = reversed_string == string_r
    return string_r, is_palindrome