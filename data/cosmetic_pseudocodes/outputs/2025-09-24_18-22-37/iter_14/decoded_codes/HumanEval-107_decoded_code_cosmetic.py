from typing import Tuple


def even_odd_palindrome(m: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        str_x: str = str(x)
        rev_str_x: str = ""
        j: int = len(str_x) - 1
        while j >= 0:
            rev_str_x += str_x[j]
            j -= 1
        return str_x == rev_str_x

    p_count: int = 0
    q_count: int = 0
    k: int = 1

    while k <= m:
        mod_val: int = k % 2
        flag_pal: bool = is_palindrome(k)

        if flag_pal:
            if mod_val == 0:
                p_count += 1
            else:
                q_count += 1
        k += 1

    return (p_count, q_count)