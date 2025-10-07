from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_num: str = str(number)
        rev_num: str = ""
        for idx in range(len(str_num) - 1, -1, -1):
            rev_num += str_num[idx]
        return rev_num == str_num

    count_even_palindromes: int = 0
    count_odd_palindromes: int = 0
    counter: int = 1

    while counter <= n:
        if is_palindrome(counter):
            if counter % 2 == 0:
                count_even_palindromes += 1
            else:
                count_odd_palindromes += 1
        counter += 1

    return count_even_palindromes, count_odd_palindromes