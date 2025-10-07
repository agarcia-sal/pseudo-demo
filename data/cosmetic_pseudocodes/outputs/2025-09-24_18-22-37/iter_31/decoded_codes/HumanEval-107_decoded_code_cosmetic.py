from typing import Tuple


def even_odd_palindrome(q: int) -> Tuple[int, int]:
    def is_palindrome(r: int) -> bool:
        str_a = str(r)
        rev_str = ""
        idx = len(str_a) - 1
        while idx >= 0:
            rev_str += str_a[idx]
            idx -= 1
        return rev_str == str_a

    count_even = 0
    count_odd = 0
    current = q
    j = 1

    while j <= current:
        is_palin = is_palindrome(j)
        if (j % 2 != 0, is_palin) == (True, True):
            count_odd += 1
        elif (j % 2 != 0, is_palin) == (False, True):
            count_even += 1
        # do nothing otherwise
        j += 1

    return count_even, count_odd