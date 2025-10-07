from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        string_form: str = str(number)
        reversed_form: str = "".join(string_form[idx] for idx in range(len(string_form) - 1, -1, -1))
        return reversed_form == string_form

    odd_palindromes: int = 0
    even_palindromes: int = 0
    current: int = 1

    while current <= n:
        if is_palindrome(current):
            if current % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1
        current += 1

    return even_palindromes, odd_palindromes