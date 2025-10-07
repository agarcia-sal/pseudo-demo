from typing import Tuple


def reverse_delete(string_x: str, string_y: str) -> Tuple[str, str]:
    filtered_chars = [c for c in string_x if c not in string_y]
    joined_str = "".join(filtered_chars)
    reversed_str = ""
    pos = len(joined_str) - 1
    while pos >= 0:
        reversed_str += joined_str[pos]
        pos -= 1
    return joined_str, reversed_str