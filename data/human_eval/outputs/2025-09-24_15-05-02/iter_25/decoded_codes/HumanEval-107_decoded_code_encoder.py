from typing import Tuple


def even_odd_palindrome(integer_n: int) -> Tuple[int, int]:
    def is_palindrome(integer_x: int) -> bool:
        s = str(integer_x)
        return s == s[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for integer_i in range(1, integer_n + 1):
        if is_palindrome(integer_i):
            if integer_i % 2 == 1:
                odd_palindrome_count += 1
            else:
                even_palindrome_count += 1

    return even_palindrome_count, odd_palindrome_count