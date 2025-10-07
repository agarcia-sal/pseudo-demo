from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s = str(number)

        def helper(str_: str, left: int, right: int) -> bool:
            if left >= right:
                return True
            if str_[left] != str_[right]:
                return False
            return helper(str_, left + 1, right - 1)

        return helper(s, 0, len(s) - 1)

    x1 = 0  # count palindromes of even numbers
    x2 = 0  # count palindromes of odd numbers
    j = 1

    while j <= n:
        if j % 2 != 0:
            if is_palindrome(j):
                x2 += 1
        else:
            if is_palindrome(j):
                x1 += 1
        j += 1

    return x1, x2