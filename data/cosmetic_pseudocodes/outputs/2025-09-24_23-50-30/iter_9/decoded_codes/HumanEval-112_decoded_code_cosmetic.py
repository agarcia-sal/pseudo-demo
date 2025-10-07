from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    list_a: list[str] = [char_x for char_x in string_s if char_x not in string_c]
    string_s = "".join(list_a)
    rev_s = "".join(string_s[i - 1] for i in range(len(string_s), 0, -1))
    return string_s, rev_s == string_s