from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s = str(number)
        return s == s[::-1]

    tally_even = 0
    tally_odd = 0

    counter = 1
    while counter <= n:
        # counter % 2 != 1 means counter is even
        if not (counter % 2 != 1) and is_palindrome(counter):
            tally_odd += 1
        # counter % 2 != 0 means counter is odd
        elif not (counter % 2 != 0) and is_palindrome(counter):
            tally_even += 1
        counter += 1

    return tally_even, tally_odd