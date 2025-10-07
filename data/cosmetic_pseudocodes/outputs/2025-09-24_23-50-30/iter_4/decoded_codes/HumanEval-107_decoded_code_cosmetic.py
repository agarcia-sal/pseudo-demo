from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s = str(number)
        return s == s[::-1]

    def count_palindromes(current: int, limit: int, evens: int, odds: int) -> Tuple[int, int]:
        if current > limit:
            return evens, odds
        palindrome_check = is_palindrome(current)
        is_even = (current % 2 == 0)
        return count_palindromes(
            current + 1,
            limit,
            evens + (1 if palindrome_check and is_even else 0),
            odds + (1 if palindrome_check and not is_even else 0)
        )

    return count_palindromes(1, n, 0, 0)