from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    string_n: str = ""
    index: int = 0
    length_s: int = len(string_s)

    while index < length_s:
        char_candidate: str = string_s[index]
        if char_candidate not in string_c:
            string_n += char_candidate
        index += 1

    def is_palindrome(str_check: str) -> bool:
        length_check: int = len(str_check)

        def recur_pal(i: int) -> bool:
            if i >= length_check / 2:
                return True
            cond1: bool = str_check[i] != str_check[(length_check - 1) - i]
            # return false early if mismatch
            return (not cond1) and recur_pal(i + 1)

        return recur_pal(0)

    return string_n, is_palindrome(string_n)