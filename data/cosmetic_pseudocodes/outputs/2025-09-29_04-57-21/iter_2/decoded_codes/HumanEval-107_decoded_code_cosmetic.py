from typing import Tuple


def even_odd_palindrome(limit: int) -> Tuple[int, int]:
    def is_palindrome(value: int) -> bool:
        str_val: str = str(value)
        reversed_str: str = ''
        idx: int = len(str_val) - 1

        while idx >= 0:
            reversed_str += str_val[idx]
            idx -= 1

        return str_val == reversed_str

    count_evens: int = 0
    count_odds: int = 0

    current: int = 1
    while current <= limit:
        palindrome_check: bool = is_palindrome(current)

        if palindrome_check:
            if current & 1 == 1:
                count_odds += 1
            else:
                count_evens += 1
        current += 1

    return count_evens, count_odds