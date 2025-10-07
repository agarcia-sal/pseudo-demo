from typing import Tuple


def even_odd_palindrome(x: int) -> Tuple[int, int]:
    def is_palindrome(y: int) -> bool:
        str_form: str = str(y)
        reversed_str: str = ''
        idx: int = len(str_form) - 1
        while idx >= 0:
            reversed_str += str_form[idx]
            idx -= 1
        return str_form == reversed_str

    cnt_even_palindrome: int = 0
    cnt_odd_palindrome: int = 0
    counter: int = 1

    while counter <= x:
        if (counter % 2) != 0:
            if is_palindrome(counter):
                cnt_odd_palindrome += 1
        else:
            if is_palindrome(counter):
                cnt_even_palindrome += 1
        counter += 1

    return cnt_even_palindrome, cnt_odd_palindrome