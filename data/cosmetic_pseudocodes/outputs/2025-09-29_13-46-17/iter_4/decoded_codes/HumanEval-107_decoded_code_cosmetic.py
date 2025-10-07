from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def palindrome_check(value: int) -> bool:
        value_str = str(value)
        reversed_str = value_str[::-1]  # Reverse the string using slicing
        return value_str == reversed_str

    accumulator_evenPal: int = 0
    accumulator_oddPal: int = 0

    counter: int = 1

    while counter <= n:
        if counter % 2 != 0:
            if palindrome_check(counter):
                accumulator_oddPal += 1
        else:
            if palindrome_check(counter):
                accumulator_evenPal += 1
        counter += 1

    return accumulator_evenPal, accumulator_oddPal