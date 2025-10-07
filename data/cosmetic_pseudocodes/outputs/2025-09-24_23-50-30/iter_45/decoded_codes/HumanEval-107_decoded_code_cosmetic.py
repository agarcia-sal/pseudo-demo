from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_form: str = str(number)
        reversed_str: str = "".join(str_form[i] for i in range(len(str_form) - 1, -1, -1))
        return str_form == reversed_str

    count_evens: int = 0
    count_odds: int = 0

    current: int = 1
    while current <= n:
        if current % 2 == 1:
            if is_palindrome(current):
                count_odds += 1
        else:
            if is_palindrome(current):
                count_evens += 1
        current += 1

    return count_evens, count_odds