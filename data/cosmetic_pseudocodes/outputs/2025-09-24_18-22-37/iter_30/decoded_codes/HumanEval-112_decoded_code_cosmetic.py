from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    temp_a = ""
    iterator_j = 0
    while iterator_j < len(string_s):
        current_chr = string_s[iterator_j]
        if current_chr not in string_c:
            temp_a += current_chr
        iterator_j += 1
    reversed_b = ""
    index_m = len(temp_a) - 1
    while index_m >= 0:
        reversed_b += temp_a[index_m]
        index_m -= 1
    is_palindrome = reversed_b == temp_a
    return temp_a, is_palindrome