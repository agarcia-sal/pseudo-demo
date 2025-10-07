from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num: str = str(number)
        reversed_str: str = ""
        idx: int = len(str_num) - 1
        while idx >= 0:
            reversed_str += str_num[idx]
            idx -= 1
        return str_num == reversed_str

    count_even_palindromes: int = 0
    count_odd_palindromes: int = 0

    current_value: int = 1
    while current_value <= n:
        is_current_palindrome = is_palindrome(current_value)
        if not (current_value % 2 != 1):  # current_value is odd
            if is_current_palindrome:
                count_odd_palindromes += 1
        else:  # current_value is even
            if is_current_palindrome:
                count_even_palindromes += 1
        current_value += 1

    return count_even_palindromes, count_odd_palindromes