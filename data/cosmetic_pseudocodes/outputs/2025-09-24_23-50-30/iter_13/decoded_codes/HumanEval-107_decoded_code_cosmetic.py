from typing import Tuple

def even_odd_palindrome(limit: int) -> Tuple[int, int]:
    count_even: int = 0
    count_odd: int = 0

    for current in range(1, limit + 1):
        s = str(current)
        if (current % 2 == 1) and (s == s[::-1]):
            count_odd += 1
        elif (current % 2 == 0) and (s == s[::-1]):
            count_even += 1

    return count_even, count_odd