from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        return str_num == str_num[::-1]

    even_palindromes = 0
    odd_palindromes = 0

    for value in range(1, n + 1):
        if is_palindrome(value):
            if value % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return even_palindromes, odd_palindromes