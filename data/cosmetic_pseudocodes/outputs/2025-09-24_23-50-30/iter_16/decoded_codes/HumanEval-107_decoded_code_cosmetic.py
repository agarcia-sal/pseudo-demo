from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s: str = str(number)
        reversed_s = [s[idx] for idx in range(len(s) - 1, -1, -1)]  # reverse by indices
        return s == ''.join(reversed_s)

    def count_palindromes(current: int, max_val: int, evens: int, odds: int) -> Tuple[int, int]:
        if current > max_val:
            return evens, odds

        if is_palindrome(current):
            if current % 2 != 0:
                odds += 1
            else:
                evens += 1

        return count_palindromes(current + 1, max_val, evens, odds)

    return count_palindromes(1, n, 0, 0)