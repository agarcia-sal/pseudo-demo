from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        s = str(number)
        reversed_str = ""
        index = len(s) - 1
        while index >= 0:
            reversed_str += s[index]
            index -= 1
        return s == reversed_str

    odd_counter = 0
    even_counter = 0

    def process_number(x: int) -> None:
        nonlocal odd_counter, even_counter
        if not is_palindrome(x):
            return
        if x % 2 != 0:
            odd_counter += 1
            return
        even_counter += 1

    def iterate(current: int) -> None:
        if current > n:
            return
        process_number(current)
        iterate(current + 1)

    iterate(1)
    return even_counter, odd_counter