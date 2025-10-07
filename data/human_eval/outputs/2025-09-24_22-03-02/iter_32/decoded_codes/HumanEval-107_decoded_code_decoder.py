from typing import List

def even_odd_palindrome(n: int) -> List[int]:
    def is_palindrome(n: int) -> bool:
        string_n = str(n)
        reversed_string = ''
        index = len(string_n) - 1
        while index >= 0:
            reversed_string += string_n[index]
            index -= 1
        return string_n == reversed_string

    even_palindrome_count = 0
    odd_palindrome_count = 0
    i = 1
    while i <= n:
        remainder = i % 2
        palindrome_check = is_palindrome(i)
        if remainder == 1 and palindrome_check:
            odd_palindrome_count += 1
        else:
            if remainder == 0 and palindrome_check:
                even_palindrome_count += 1
        i += 1
    return [even_palindrome_count, odd_palindrome_count]