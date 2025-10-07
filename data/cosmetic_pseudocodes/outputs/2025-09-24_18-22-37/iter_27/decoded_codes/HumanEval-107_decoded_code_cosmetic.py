from typing import Tuple


def even_odd_palindrome(p: int) -> Tuple[int, int]:
    def is_palindrome(q: int) -> bool:
        str_form = str(q)
        rev_str = str_form[::-1]
        return str_form == rev_str

    beta = 0  # count of even palindrome numbers
    alpha = 0  # count of odd palindrome numbers

    x = 1
    while x <= p:
        u = x % 2
        v = is_palindrome(x)
        if u != 1:
            if v:
                beta += 1
        else:
            if v:
                alpha += 1
        x += 1

    return beta, alpha