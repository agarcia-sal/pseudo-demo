from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    count_even = 0
    count_odd = 0
    index = 1

    while index <= n:
        mod_val = index % 2
        palindrome_check = is_palindrome(index)
        if mod_val == 0:
            if palindrome_check:
                count_even += 1
        else:  # mod_val == 1
            if palindrome_check:
                count_odd += 1
        index += 1

    return count_even, count_odd