from typing import Tuple


def even_odd_palindrome(x: int) -> Tuple[int, int]:
    def is_palindrome(y: int) -> bool:
        str_val = str(y)
        reversed_str = ""
        index = len(str_val)
        while index > 0:
            reversed_str += str_val[index - 1]
            index -= 1
        return str_val == reversed_str

    count_even_pal = 0
    count_odd_pal = 0

    counter = 1
    while counter <= x:
        remainder = counter % 2

        if remainder != 0:
            if is_palindrome(counter):
                count_odd_pal += 1
        else:
            if is_palindrome(counter):
                count_even_pal += 1

        counter += 1

    return count_even_pal, count_odd_pal