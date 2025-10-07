from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        idx_start, idx_end = 0, len(str_num) - 1

        while idx_start < idx_end:
            if str_num[idx_start] != str_num[idx_end]:
                return False
            idx_start += 1
            idx_end -= 1

        return True

    count_even_palindromes = 0
    count_odd_palindromes = 0
    current_val = 1

    while current_val <= n:
        if not is_palindrome(current_val):
            current_val += 1
            continue

        if current_val % 2 == 0:
            count_even_palindromes += 1
        else:
            count_odd_palindromes += 1

        current_val += 1

    return count_even_palindromes, count_odd_palindromes