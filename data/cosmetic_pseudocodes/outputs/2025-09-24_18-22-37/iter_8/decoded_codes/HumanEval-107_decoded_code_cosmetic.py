from typing import Tuple


def even_odd_palindrome(m: int) -> Tuple[int, int]:

    def is_palindrome(x: int) -> bool:
        str_x = str(x)
        rev_str_x = ""
        idx = len(str_x) - 1
        while idx >= 0:
            rev_str_x += str_x[idx]
            idx -= 1
        return str_x == rev_str_x

    count_even_pal = 0
    count_odd_pal = 0

    counter = 1
    while counter <= m:
        remainder = counter % 2

        if remainder == 0:
            if is_palindrome(counter):
                count_even_pal += 1
        elif remainder == 1:
            if is_palindrome(counter):
                count_odd_pal += 1

        counter += 1

    return count_even_pal, count_odd_pal