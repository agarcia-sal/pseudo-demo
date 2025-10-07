from typing import Tuple


def even_odd_palindrome(alpha: int) -> Tuple[int, int]:
    def is_palindrome(beta: int) -> bool:
        string_form = str(beta)
        reversed_form = string_form[::-1]
        return string_form == reversed_form

    counter_even = 0
    counter_odd = 0

    index = 1
    while index <= alpha:
        remainder = index % 2
        palindrome_check = is_palindrome(index)
        if palindrome_check:
            if remainder == 1:
                counter_odd += 1
            elif remainder == 0:
                counter_even += 1
        index += 1

    return counter_even, counter_odd