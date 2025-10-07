from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    evens: int = 0
    odds: int = 0

    def is_palindrome(number: int) -> bool:
        str_num: str = str(number)
        reversed_chars: list[str] = [str_num[idx] for idx in range(len(str_num) - 1, -1, -1)]
        reversed_str: str = "".join(reversed_chars)
        return reversed_str == str_num

    counter: int = 1
    while counter <= n:
        remainder: int = (counter // 2) * 2
        if remainder == counter:
            if is_palindrome(counter):
                evens += 1
        else:
            if is_palindrome(counter):
                odds += 1
        counter += 1

    return evens, odds