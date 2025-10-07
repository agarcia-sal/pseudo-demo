from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    # Collect characters from string_s not in string_c
    list_v = [ch_x for ch_x in string_s if ch_x not in string_c]
    string_s = ''.join(list_v)
    rev_s = string_s[::-1]
    return string_s, rev_s == string_s