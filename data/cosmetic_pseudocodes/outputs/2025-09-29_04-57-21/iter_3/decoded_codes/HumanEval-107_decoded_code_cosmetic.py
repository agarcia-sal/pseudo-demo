from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        reversed_str = ''.join(str_num[i] for i in range(len(str_num) - 1, -1, -1))
        return str_num == reversed_str

    count_even_palindromes = 0
    count_odd_palindromes = 0

    current_num = 1
    while current_num <= n:
        if is_palindrome(current_num):
            if current_num % 2 != 0:
                count_odd_palindromes += 1
            else:
                count_even_palindromes += 1
        current_num += 1

    return count_even_palindromes, count_odd_palindromes