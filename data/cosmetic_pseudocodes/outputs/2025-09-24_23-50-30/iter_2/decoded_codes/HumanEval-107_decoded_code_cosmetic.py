from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s: str = str(number)
        left: int = 0
        right: int = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    count_even: int = 0
    count_odd: int = 0
    current: int = n

    while current > 0:
        if current % 2 != 0 and is_palindrome(current):
            count_odd += 1
        elif current % 2 == 0 and is_palindrome(current):
            count_even += 1
        current -= 1

    return count_even, count_odd