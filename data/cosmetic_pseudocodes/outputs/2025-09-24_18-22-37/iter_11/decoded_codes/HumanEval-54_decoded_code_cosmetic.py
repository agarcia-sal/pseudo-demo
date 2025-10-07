from typing import Set


def same_chars(string_alpha: str, string_beta: str) -> bool:
    set_m: Set[str] = set()
    set_n: Set[str] = set()

    index_p: int = 0
    while index_p < len(string_alpha):
        char_q: str = string_alpha[index_p]
        set_m.add(char_q)
        index_p += 1

    cursor_r: int = 0
    while cursor_r < len(string_beta):
        char_s: str = string_beta[cursor_r]
        set_n.add(char_s)
        cursor_r += 1

    bool_result: bool = False
    if (set_m - set_n) == set():
        if (set_n - set_m) == set():
            bool_result = True

    return bool_result