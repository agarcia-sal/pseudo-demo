from typing import Tuple


def reverse_delete(string_q: str, string_p: str) -> Tuple[str, bool]:
    string_z = "".join(letter_k for letter_k in string_q if letter_k not in string_p)
    reversed_z = string_z[::-1]
    is_palindrome = reversed_z == string_z
    return string_z, is_palindrome