from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        rev_str_num = ''
        idx = len(str_num) - 1
        while idx >= 0:
            rev_str_num += str_num[idx]
            idx -= 1
        return str_num == rev_str_num

    count_evens = 0
    count_odds = 0

    current = 1
    while current <= n:
        mod_result = current - ((current // 2) * 2)  # equivalent to current % 2 but per pseudocode
        if mod_result != 0:
            if is_palindrome(current):
                count_odds += 1
        else:
            if is_palindrome(current):
                count_evens += 1
        current += 1

    return count_evens, count_odds