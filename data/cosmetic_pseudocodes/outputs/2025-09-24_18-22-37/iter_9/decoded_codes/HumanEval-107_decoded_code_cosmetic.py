from typing import Tuple


def even_odd_palindrome(x: int) -> Tuple[int, int]:
    def is_palindrome(y: int) -> bool:
        str_val: str = str(y)
        rev_str: str = ''
        idx: int = len(str_val) - 1
        while idx >= 0:
            rev_str += str_val[idx]
            idx -= 1
        return str_val == rev_str

    count_even_pal: int = 0
    count_odd_pal: int = 0
    num: int = 1

    while True:
        if num > x:
            break

        remainder_mod_2: int = num % 2
        palindrome_flag: bool = is_palindrome(num)

        if remainder_mod_2 == 1:
            if palindrome_flag:
                count_odd_pal += 1
        else:
            if palindrome_flag:
                count_even_pal += 1

        num += 1

    return count_even_pal, count_odd_pal