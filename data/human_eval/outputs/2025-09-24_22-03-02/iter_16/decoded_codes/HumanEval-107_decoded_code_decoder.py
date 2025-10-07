from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(num: int) -> bool:
        string_representation = str(num)
        reversed_string = ''
        for index in range(len(string_representation) - 1, -1, -1):
            reversed_string += string_representation[index]
        return string_representation == reversed_string

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        remainder = i % 2
        if remainder == 1 and is_palindrome(i):
            odd_palindrome_count += 1
        elif remainder == 0 and is_palindrome(i):
            even_palindrome_count += 1

    return (even_palindrome_count, odd_palindrome_count)