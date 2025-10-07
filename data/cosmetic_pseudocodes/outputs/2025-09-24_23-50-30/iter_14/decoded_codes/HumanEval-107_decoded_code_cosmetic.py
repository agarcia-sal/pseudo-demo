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

    count_even = 0
    count_odd = 0
    current = 1
    while current <= n:
        if not is_palindrome(current):
            current += 1
            continue
        if current % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        current += 1

    return count_even, count_odd