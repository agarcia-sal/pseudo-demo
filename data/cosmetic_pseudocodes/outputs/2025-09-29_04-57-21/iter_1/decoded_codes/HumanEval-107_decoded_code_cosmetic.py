from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(num: int) -> bool:
        str_num: str = str(num)
        rev_str_num: str = ''
        for idx in range(len(str_num) - 1, -1, -1):
            rev_str_num += str_num[idx]
        return str_num == rev_str_num

    evens_found: int = 0
    odds_found: int = 0

    counter: int = 1
    while counter <= n:
        if is_palindrome(counter):
            if counter % 2 == 0:
                evens_found += 1
            else:
                odds_found += 1
        counter += 1

    return evens_found, odds_found