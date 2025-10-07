from typing import Tuple


def even_odd_palindrome(m: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        text = str(x)
        reversed_text = ''.join(text[i] for i in range(len(text) - 1, -1, -1))
        return text == reversed_text

    total_even = 0
    total_odd = 0

    current = 1
    while current <= m:
        if not (current % 2 != 1):  # current is odd
            if is_palindrome(current):
                total_odd += 1
        elif not (current % 2 != 0):  # current is even
            if is_palindrome(current):
                total_even += 1
        current += 1

    return total_even, total_odd