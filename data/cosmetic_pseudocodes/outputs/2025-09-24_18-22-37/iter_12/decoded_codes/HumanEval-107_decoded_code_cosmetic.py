from typing import Tuple


def even_odd_palindrome(xz: int) -> Tuple[int, int]:
    def is_palindrome(zq: int) -> bool:
        str_val = str(zq)
        rev_str = str_val[::-1]
        return str_val == rev_str

    empc = 0
    opmc = 0
    idx = 1

    while idx <= xz:
        rem = idx % 2
        if rem == 1:
            if is_palindrome(idx):
                opmc += 1
        else:
            if rem == 0:
                if is_palindrome(idx):
                    empc += 1
        idx += 1

    return empc, opmc