from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    buffer_t: str = ''
    for index_i in range(1, len(string_s) + 1):
        char = string_s[index_i - 1]  # Adjusting for 1-based index in pseudocode
        if char not in string_c:
            buffer_t += char
    rev_flag: bool = (buffer_t == buffer_t[::-1])
    return buffer_t, rev_flag