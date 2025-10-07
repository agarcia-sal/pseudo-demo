from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        num_str = str(number)
        reversed_str = "".join(num_str[i] for i in range(len(num_str)-1, -1, -1))
        return num_str == reversed_str

    even_palindromes = 0
    odd_palindromes = 0

    current = 1
    while current <= n:
        if is_palindrome(current):
            if current % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1
        current += 1

    return even_palindromes, odd_palindromes