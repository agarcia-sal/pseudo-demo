from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        reversed_str = ''
        idx = len(str_num) - 1
        while idx >= 0:
            reversed_str += str_num[idx]
            idx -= 1
        return str_num == reversed_str

    count_even_palindromes = 0
    count_odd_palindromes = 0

    current = 1
    while current <= n:
        is_odd = (current % 2 != 0)
        if is_palindrome(current):
            if is_odd:
                count_odd_palindromes += 1
            else:
                count_even_palindromes += 1
        current += 1

    return count_even_palindromes, count_odd_palindromes