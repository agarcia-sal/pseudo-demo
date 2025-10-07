from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    list_alpha: list[str] = [
        char_gamma
        for char_gamma in string_s
        if char_gamma not in string_c
    ]
    string_delta: str = "".join(list_alpha)
    return string_delta, string_delta == string_delta[::-1]