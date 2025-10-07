from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(n: int) -> bool:
        string_n = str(n)
        reversed_string = ''
        index = len(string_n) - 1
        while index >= 0:
            reversed_string += string_n[index]
            index -= 1
        if string_n == reversed_string:
            return True
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0

    i = 1
    while i <= n:
        palindrome_check = is_palindrome(i)
        if (i % 2) == 1 and palindrome_check is True:
            odd_palindrome_count += 1
        elif (i % 2) == 0 and palindrome_check is True:
            even_palindrome_count += 1
        i += 1

    return (even_palindrome_count, odd_palindrome_count)