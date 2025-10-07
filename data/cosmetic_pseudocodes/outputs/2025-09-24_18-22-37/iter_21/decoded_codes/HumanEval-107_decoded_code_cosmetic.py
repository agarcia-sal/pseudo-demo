from typing import Tuple


def even_odd_palindrome(x: int) -> Tuple[int, int]:
    def is_palindrome(y: int) -> bool:
        string_form = str(y)
        reversed_form = ''
        index = len(string_form)
        while index >= 1:
            reversed_form += string_form[index - 1]
            index -= 1
        return string_form == reversed_form

    total_even_palindromes = 0
    total_odd_palindromes = 0

    current_number = 1
    while current_number <= x:
        is_curr_palindrome = is_palindrome(current_number)
        remainder = current_number % 2
        if remainder == 1:
            if is_curr_palindrome:
                total_odd_palindromes += 1
        else:  # remainder == 0
            if is_curr_palindrome:
                total_even_palindromes += 1
        current_number += 1

    return total_even_palindromes, total_odd_palindromes