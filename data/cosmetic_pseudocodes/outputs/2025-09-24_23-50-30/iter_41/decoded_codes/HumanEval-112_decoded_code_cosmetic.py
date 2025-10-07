from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    list_a = [ch for ch in string_s if ch not in string_c]

    string_b = ''.join(list_a)

    def check_palindrome(str_p: str) -> bool:
        if len(str_p) <= 1:
            return True
        if str_p[0] == str_p[-1]:
            return check_palindrome(str_p[1:-1])
        return False

    return string_b, check_palindrome(string_b)