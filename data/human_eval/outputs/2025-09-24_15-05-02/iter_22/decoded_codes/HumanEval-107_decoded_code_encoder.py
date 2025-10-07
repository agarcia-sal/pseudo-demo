from typing import Tuple


def even_odd_palindrome(upper_limit: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s = str(number)
        return s == s[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for current_number in range(1, upper_limit + 1):
        if current_number % 2 == 1 and is_palindrome(current_number):
            odd_palindrome_count += 1
        elif current_number % 2 == 0 and is_palindrome(current_number):
            even_palindrome_count += 1

    return even_palindrome_count, odd_palindrome_count