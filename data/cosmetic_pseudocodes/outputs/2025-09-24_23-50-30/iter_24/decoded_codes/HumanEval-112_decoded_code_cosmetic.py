from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    list_m: list[str] = []
    index_p: int = 0
    while index_p < len(string_s):
        char_q: str = string_s[index_p]
        if char_q not in string_c:
            list_m.append(char_q)
        index_p += 1

    string_x: str = ""
    # Recursive function to concatenate characters from list_m to string_x
    def concat_chars(num_r: int) -> None:
        nonlocal string_x
        if num_r == len(list_m):
            return
        string_x += list_m[num_r]
        concat_chars(num_r + 1)

    concat_chars(0)

    bool_y: bool = True
    num_u: int = 0
    length_half: float = len(string_x) / 2
    while num_u < length_half:
        if string_x[num_u] != string_x[len(string_x) - 1 - num_u]:
            bool_y = False
            break
        num_u += 1

    return string_x, bool_y