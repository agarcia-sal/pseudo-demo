from typing import Tuple


def even_odd_palindrome(k: int) -> Tuple[int, int]:

    def is_palindrome(p: int) -> bool:
        str_rep = str(p)
        rev_str = ""
        idx = len(str_rep)
        while idx > 0:
            rev_str += str_rep[idx - 1]
            idx -= 1
        return str_rep == rev_str

    count_even_pal: int = 0
    count_odd_pal: int = 0
    counter: int = 1

    while True:
        if counter % 2 != 0:
            if is_palindrome(counter):
                count_odd_pal += 1
        else:
            if is_palindrome(counter):
                count_even_pal += 1
        counter += 1
        if counter > k:
            break

    return count_even_pal, count_odd_pal