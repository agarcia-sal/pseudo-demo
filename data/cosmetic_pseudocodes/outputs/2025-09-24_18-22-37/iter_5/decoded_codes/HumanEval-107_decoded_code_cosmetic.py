from typing import Tuple

def even_odd_palindrome(x: int) -> Tuple[int, int]:
    def is_palindrome(y: int) -> bool:
        str_form = str(y)
        reversed_str = ''
        index = len(str_form) - 1
        while index >= 0:
            reversed_str += str_form[index]
            index -= 1
        return str_form == reversed_str

    count_even_pal = 0
    count_odd_pal = 0

    idx = 1
    while idx <= x:
        remainder = idx % 2
        palindrome_check = is_palindrome(idx)
        if remainder == 1:
            if palindrome_check:
                count_odd_pal += 1
        elif remainder == 0:
            if palindrome_check:
                count_even_pal += 1
        idx += 1

    return count_even_pal, count_odd_pal