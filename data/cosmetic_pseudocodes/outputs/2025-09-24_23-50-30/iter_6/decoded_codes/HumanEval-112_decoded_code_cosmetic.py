from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    list_d: list[str] = []
    idx: int = 0
    while idx < len(string_s):
        ch: str = string_s[idx]
        if ch not in string_c:
            list_d.append(ch)
        idx += 1

    filtered_str: str = ''.join(list_d)

    reversed_str: str = ''
    pos: int = len(filtered_str) - 1
    while pos >= 0:
        reversed_str += filtered_str[pos]
        pos -= 1

    return filtered_str, reversed_str == filtered_str