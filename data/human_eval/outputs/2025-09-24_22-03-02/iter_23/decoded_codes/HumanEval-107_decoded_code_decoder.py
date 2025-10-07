from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(n: int) -> bool:
        str_n = []
        i = 0
        str_n = list(str(n))
        reversed_str_n = []
        j = len(str_n) - 1
        while j >= 0:
            reversed_str_n.append(str_n[j])
            j -= 1
        if len(str_n) == len(reversed_str_n) and all(str_n[k] == reversed_str_n[k] for k in range(len(str_n))):
            return True
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0

    i = 1
    while i <= n:
        current_is_palindrome = is_palindrome(i)
        if i % 2 == 1 and current_is_palindrome is True:
            odd_palindrome_count += 1
        elif i % 2 == 0 and current_is_palindrome is True:
            even_palindrome_count += 1
        i += 1

    return (even_palindrome_count, odd_palindrome_count)