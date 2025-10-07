from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = []
    index_k = 0

    while index_k < len(string_s):
        char_x = string_s[index_k]
        if char_x not in string_c:
            filtered_chars.append(char_x)
        index_k += 1

    processed_string = ''.join(filtered_chars)

    reversed_matched = True
    pos_m = 0
    limit_n = len(processed_string) - 1

    while pos_m < limit_n and reversed_matched:
        if processed_string[pos_m] != processed_string[limit_n]:
            reversed_matched = False
        else:
            pos_m += 1
            limit_n -= 1

    return processed_string, reversed_matched