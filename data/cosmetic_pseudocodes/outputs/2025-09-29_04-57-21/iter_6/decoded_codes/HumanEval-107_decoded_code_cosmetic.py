from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        length = len(str_num)
        for idx in range(length // 2):
            if str_num[idx] != str_num[length - idx - 1]:
                return False
        return True

    count_even_palindromes = 0
    count_odd_palindromes = 0

    current_value = 1
    while current_value <= n:
        if current_value % 2 != 0:
            if is_palindrome(current_value):
                count_odd_palindromes += 1
        else:
            if is_palindrome(current_value):
                count_even_palindromes += 1
        current_value += 1

    return count_even_palindromes, count_odd_palindromes