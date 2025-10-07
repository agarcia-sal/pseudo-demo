from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        str_form = str(x)
        rev_str = str_form[::-1]
        return str_form == rev_str

    count_even = 0
    count_odd = 0
    index = 1

    while index <= n:
        modulo_result = index % 2
        palindrome_check = is_palindrome(index)

        if modulo_result == 0:
            if palindrome_check:
                count_even += 1
        elif modulo_result == 1:
            if palindrome_check:
                count_odd += 1
        # default case deliberately does nothing

        index += 1

    return count_even, count_odd