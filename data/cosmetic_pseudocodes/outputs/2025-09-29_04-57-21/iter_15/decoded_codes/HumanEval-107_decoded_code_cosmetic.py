from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        reversed_str = ""
        idx = len(str_num) - 1
        while idx >= 0:
            reversed_str += str_num[idx]
            idx -= 1
        return reversed_str == str_num

    total_even_palindromes = 0
    total_odd_palindromes = 0

    current_val = 1
    while current_val <= n:
        is_current_palindrome = is_palindrome(current_val)
        odd_test = (current_val % 2) != 0
        if is_current_palindrome:
            if odd_test:
                total_odd_palindromes += 1
            else:
                total_even_palindromes += 1
        current_val += 1

    return total_even_palindromes, total_odd_palindromes