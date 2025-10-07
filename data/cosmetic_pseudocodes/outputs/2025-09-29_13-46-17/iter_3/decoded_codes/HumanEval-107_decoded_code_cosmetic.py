from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    countEvens: int = 0
    countOdds: int = 0

    def is_palindrome(number: int) -> bool:
        s = str(number)
        return s == s[::-1]

    def check_number(currentIndex: int) -> None:
        nonlocal countEvens, countOdds
        if currentIndex > n:
            return

        if is_palindrome(currentIndex):
            if currentIndex % 2 == 0:
                countEvens += 1
            else:
                countOdds += 1

        check_number(currentIndex + 1)

    check_number(1)
    return countEvens, countOdds