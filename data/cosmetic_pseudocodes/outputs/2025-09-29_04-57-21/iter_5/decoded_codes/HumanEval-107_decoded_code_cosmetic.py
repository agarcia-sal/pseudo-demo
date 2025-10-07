from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s = str(number)
        return s == s[::-1]

    tally_even: int = 0
    tally_odd: int = 0

    index: int = 1
    while index <= n:
        if is_palindrome(index):
            if index % 2 != 0:
                tally_odd += 1
            else:
                tally_even += 1
        index += 1

    return tally_even, tally_odd