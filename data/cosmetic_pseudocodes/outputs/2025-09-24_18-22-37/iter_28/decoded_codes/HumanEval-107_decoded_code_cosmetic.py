from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(num: int) -> bool:
        str_num = str(num)
        rev_str = str_num[::-1]
        return str_num == rev_str

    count_even = 0
    count_odd = 0

    idx = 1
    while idx <= n:
        remainder_even = idx % 2
        palindrome_check = is_palindrome(idx)

        if remainder_even == 0:
            if palindrome_check:
                count_even += 1
        else:  # remainder_even == 1
            if palindrome_check:
                count_odd += 1

        idx += 1

    return count_even, count_odd