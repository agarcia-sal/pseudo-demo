from typing import Tuple


def even_odd_palindrome(k: int) -> Tuple[int, int]:
    def is_palindrome(m: int) -> bool:
        s = str(m)
        t = ""
        for j in range(len(s) - 1, -1, -1):
            t += s[j]
        return s == t

    def loop_recursive(x: int, e_cnt: int, o_cnt: int) -> Tuple[int, int]:
        if x > k:
            return e_cnt, o_cnt
        if x % 2 == 0:
            return loop_recursive(x + 1, e_cnt + (1 if is_palindrome(x) else 0), o_cnt)
        else:
            return loop_recursive(x + 1, e_cnt, o_cnt + (1 if is_palindrome(x) else 0))

    return loop_recursive(1, 0, 0)