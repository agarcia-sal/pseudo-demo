from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        rev_str = ''
        idx = len(str_num) - 1
        while idx >= 0:
            rev_str += str_num[idx]
            idx -= 1
        return rev_str == str_num

    count_even_pal = 0
    count_odd_pal = 0
    current_val = 1
    while current_val <= n:
        if current_val % 2 != 0:
            if is_palindrome(current_val):
                count_odd_pal += 1
        else:
            if is_palindrome(current_val):
                count_even_pal += 1
        current_val += 1

    return count_even_pal, count_odd_pal