from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    fresh_x = ""
    fresh_i = 1
    length_s = len(string_s)
    while fresh_i <= length_s:
        fresh_char = string_s[fresh_i - 1]  # Convert 1-based index to 0-based
        if fresh_char not in string_c:
            fresh_x += fresh_char
        fresh_i += 1

    fresh_reversed = ""
    fresh_j = len(fresh_x)
    while fresh_j != 0:
        fresh_reversed += fresh_x[fresh_j - 1]  # 1-based indexing
        fresh_j -= 1

    return fresh_x, fresh_reversed == fresh_x