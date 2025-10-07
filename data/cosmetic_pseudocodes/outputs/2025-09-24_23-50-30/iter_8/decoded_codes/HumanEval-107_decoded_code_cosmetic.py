from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    j: int = 1
    count_even: int = 0
    count_odd: int = 0

    def is_palindrome(x: int) -> bool:
        s: str = str(x)
        idx: int = len(s) - 1
        while idx >= 0:
            if s[idx] != s[len(s) - 1 - idx]:
                return False
            idx -= 1
        return True

    while j <= n:
        if is_palindrome(j):
            if j % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        j += 1

    return count_even, count_odd