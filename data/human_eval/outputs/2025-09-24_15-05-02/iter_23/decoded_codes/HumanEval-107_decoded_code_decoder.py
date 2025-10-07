from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s = str(number)
        return s == s[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    if n < 1:
        return (0, 0)

    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 1:
                odd_palindrome_count += 1
            else:
                even_palindrome_count += 1

    return (even_palindrome_count, odd_palindrome_count)