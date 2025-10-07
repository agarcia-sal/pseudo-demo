from typing import Tuple

def even_odd_palindrome(m: int) -> Tuple[int, int]:
    def is_palindrome(p: int) -> bool:
        str_val = str(p)
        rev_str = ''
        idx = len(str_val) - 1
        while idx >= 0:
            rev_str += str_val[idx]
            idx -= 1
        return str_val == rev_str

    count_even_palindrome = 0
    count_odd_palindrome = 0
    current_num = 1
    while current_num <= m:
        remainder = current_num % 2
        palindrome_check = is_palindrome(current_num)
        if remainder == 1:
            if palindrome_check:
                count_odd_palindrome += 1
        else:
            if palindrome_check:
                count_even_palindrome += 1
        current_num += 1

    return count_even_palindrome, count_odd_palindrome