from typing import Tuple


def even_odd_palindrome(q: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    count_a = 0
    count_b = 0

    idx = 1
    while idx <= q:
        if idx % 2 != 0:  # odd
            if is_palindrome(idx):
                count_b += 1
        else:  # even
            if is_palindrome(idx):
                count_a += 1
        idx += 1

    return count_a, count_b