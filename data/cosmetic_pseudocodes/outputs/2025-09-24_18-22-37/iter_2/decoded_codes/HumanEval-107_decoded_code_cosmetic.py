from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num = str(number)
        reversed_str = ''.join(str_num[idx] for idx in range(len(str_num) - 1, -1, -1))
        return str_num == reversed_str

    count_even_palindrome = 0
    count_odd_palindrome = 0
    counter = 1

    while counter <= n:
        if is_palindrome(counter):
            if counter % 2 != 0:
                count_odd_palindrome += 1
            else:
                count_even_palindrome += 1
        counter += 1

    return count_even_palindrome, count_odd_palindrome