from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        rev_str = ""
        idx = len(str_num) - 1
        while idx >= 0:
            rev_str += str_num[idx]
            idx -= 1
        return str_num == rev_str

    cnt_even = 0
    cnt_odd = 0
    curr = 1

    while curr <= n:
        remainder = curr % 2
        if remainder == 0:
            if is_palindrome(curr):
                cnt_even += 1
        else:  # remainder == 1
            if is_palindrome(curr):
                cnt_odd += 1
        curr += 1

    return cnt_even, cnt_odd