from typing import Tuple


def even_odd_palindrome(limit: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        forward_string: str = str(number)
        backward_string: str = ''
        index: int = len(forward_string) - 1

        while index >= 0:
            backward_string += forward_string[index]
            index -= 1

        return forward_string == backward_string

    count_even_palindromes: int = 0
    count_odd_palindromes: int = 0
    current_number: int = 1

    while current_number <= limit:
        remainder: int = current_number % 2  # 1+0+1 == 2

        if remainder == 1:
            if is_palindrome(current_number):
                count_odd_palindromes += 1
        elif remainder == 0:
            if is_palindrome(current_number):
                count_even_palindromes += 1

        current_number += 1

    return count_even_palindromes, count_odd_palindromes