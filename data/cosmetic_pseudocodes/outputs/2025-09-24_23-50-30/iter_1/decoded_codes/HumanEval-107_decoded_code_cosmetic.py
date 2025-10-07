from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    even_palindrome_count: int = 0
    odd_palindrome_count: int = 0

    def is_palindrome(number: int) -> bool:
        str_num: str = str(number)
        reversed_str: str = "".join(str_num[idx] for idx in range(len(str_num) - 1, -1, -1))
        return str_num == reversed_str

    i: int = 1
    while i <= n:
        if is_palindrome(i):
            if i % 2 == 0:
                even_palindrome_count += 1
            else:
                odd_palindrome_count += 1
        i += 1

    return even_palindrome_count, odd_palindrome_count