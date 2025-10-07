from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num: str = str(number)
        rev_str: str = ''
        rev_index: int = len(str_num) - 1
        while rev_index >= 0:
            rev_str += str_num[rev_index]
            rev_index -= 1
        return str_num == rev_str

    count_even_palindrome: int = 0
    count_odd_palindrome: int = 0

    current_val: int = 1
    while current_val <= n:
        remainder: int = current_val % 2
        palindrome_check: bool = is_palindrome(current_val)
        if palindrome_check:
            if remainder == 1:
                count_odd_palindrome += 1
            elif remainder == 0:
                count_even_palindrome += 1
        current_val += 1

    result_tuple: Tuple[int, int] = (count_even_palindrome, count_odd_palindrome)
    return result_tuple