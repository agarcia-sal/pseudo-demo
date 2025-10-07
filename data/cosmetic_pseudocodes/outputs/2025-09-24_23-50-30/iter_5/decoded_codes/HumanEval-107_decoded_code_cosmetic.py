from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        text = str(number)

        def check_palindrome(left: int, right: int) -> bool:
            if left >= right:
                return True
            return text[left] == text[right] and check_palindrome(left + 1, right - 1)

        return check_palindrome(0, len(text) - 1)

    def count_palindromes(current: int, max_val: int, evens: int, odds: int) -> Tuple[int, int]:
        if current > max_val:
            return evens, odds
        if is_palindrome(current):
            if current % 2 == 0:
                return count_palindromes(current + 1, max_val, evens + 1, odds)
            else:
                return count_palindromes(current + 1, max_val, evens, odds + 1)
        return count_palindromes(current + 1, max_val, evens, odds)

    return count_palindromes(1, n, 0, 0)