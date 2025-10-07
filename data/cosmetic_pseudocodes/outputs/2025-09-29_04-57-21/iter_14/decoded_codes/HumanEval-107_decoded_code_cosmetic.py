from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_form = str(number)
        rev_str = ""
        idx = len(str_form) - 1
        while idx >= 0:
            rev_str += str_form[idx]
            idx -= 1
        return str_form == rev_str

    count_even_pal = 0
    count_odd_pal = 0

    current_val = 1
    while current_val <= n:
        if not is_palindrome(current_val):
            current_val += 1
            continue
        if (current_val % 2) == 1:
            count_odd_pal += 1
        else:
            count_even_pal += 1
        current_val += 1

    return count_even_pal, count_odd_pal