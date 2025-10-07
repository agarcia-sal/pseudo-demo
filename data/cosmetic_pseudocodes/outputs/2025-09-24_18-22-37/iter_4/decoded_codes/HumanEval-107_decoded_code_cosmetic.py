from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(value: int) -> bool:
        str_val = str(value)
        rev_str = ''
        idx = len(str_val) - 1
        while idx >= 0:
            rev_str += str_val[idx]
            idx -= 1
        return str_val == rev_str

    count_even = 0
    count_odd = 0

    counter = 1
    while counter <= n:
        if counter % 2 == 1:
            if is_palindrome(counter):
                count_odd += 1
        else:
            if is_palindrome(counter):
                count_even += 1
        counter += 1

    return count_even, count_odd