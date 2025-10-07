from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s = str(number)
        return s == s[::-1]

    count_even_palindrome = 0
    count_odd_palindrome = 0
    current = 1

    while current <= n:
        if not is_palindrome(current):
            current += 1
            continue

        if current % 2 == 0:
            count_even_palindrome += 1
        else:
            count_odd_palindrome += 1

        current += 1

    return count_even_palindrome, count_odd_palindrome