from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num: str = str(number)
        str_rev: str = ""
        idx: int = len(str_num) - 1
        while idx >= 0:
            str_rev += str_num[idx]
            idx -= 1
        return str_num == str_rev

    alpha: int = 0
    beta: int = 0
    gamma: int = 1

    while gamma <= n:
        if ((gamma // 2) * 2 != gamma) and is_palindrome(gamma):
            beta += 1
        elif ((gamma // 2) * 2 == gamma) and is_palindrome(gamma):
            alpha += 1
        gamma += 1

    return alpha, beta