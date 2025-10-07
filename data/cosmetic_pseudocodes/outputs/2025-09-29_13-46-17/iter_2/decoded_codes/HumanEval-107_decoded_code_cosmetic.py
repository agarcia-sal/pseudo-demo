from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        number_str = str(number)
        reversed_str = []

        def reverse_string(index: int) -> None:
            if index < 0:
                return
            reversed_str.append(number_str[index])
            reverse_string(index - 1)

        reverse_string(len(number_str) - 1)
        return number_str == ''.join(reversed_str)

    def count_palindromes(current: int, max_val: int, even_count: int, odd_count: int) -> Tuple[int, int]:
        if current > max_val:
            return even_count, odd_count
        if is_palindrome(current):
            if current % 2 != 0:
                odd_count += 1
            else:
                even_count += 1
        return count_palindromes(current + 1, max_val, even_count, odd_count)

    return count_palindromes(1, n, 0, 0)