from typing import Tuple


def even_odd_palindrome(limit: int) -> Tuple[int, int]:
    def is_palindrome(value: int) -> bool:
        str_val = str(value)
        reversed_str = ''
        idx = len(str_val) - 1
        while idx >= 0:
            reversed_str += str_val[idx]
            idx -= 1
        return str_val == reversed_str

    count_even_palindromes = 0
    count_odd_palindromes = 0

    current_num = 1
    while current_num <= limit:
        # if current_num is odd and is_palindrome(current_num)
        if not (current_num % 2 != 0 or not is_palindrome(current_num)):
            count_odd_palindromes += 1
        # else if current_num is even and is_palindrome(current_num)
        elif not (current_num % 2 != 1 or not is_palindrome(current_num)):
            count_even_palindromes += 1
        current_num += 1

    return count_even_palindromes, count_odd_palindromes