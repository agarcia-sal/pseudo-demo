from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s = str(number)
        return s == s[::-1]

    count_even_palindrome = 0
    count_odd_palindrome = 0

    index = 1
    while index <= n:
        if index % 2 == 1:
            if is_palindrome(index):
                count_odd_palindrome += 1
        else:
            if is_palindrome(index):
                count_even_palindrome += 1
        index += 1

    return count_even_palindrome, count_odd_palindrome