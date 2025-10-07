from typing import Tuple


def even_odd_palindrome(xqz: int) -> Tuple[int, int]:
    def is_palindrome(gmj: int) -> bool:
        str_repr = str(gmj)
        rev_str = ""
        idx = len(str_repr) - 1
        while idx >= 0:
            rev_str += str_repr[idx]
            idx -= 1
        return str_repr == rev_str

    aulu = 0  # Count of even palindromes
    pqer = 0  # Count of odd palindromes
    upmg = 1

    while upmg <= xqz:
        rem = upmg % 2
        check_pal = is_palindrome(upmg)

        if rem == 1:
            if check_pal:
                pqer += 1
        elif rem == 0:
            if check_pal:
                aulu += 1
        upmg += 1

    return aulu, pqer