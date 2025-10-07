from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> Union[str, None]:

    def is_prime(n: int) -> bool:
        def check_divisor(div: int) -> bool:
            if div >= n:
                return True
            if n % div == 0:
                return False
            return check_divisor(div + 1)

        if n > 2:
            return check_divisor(2)
        if n == 2:
            return True
        if n == 0 or n == 1:
            return False
        return False

    rightBound = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    leftBound = interval1[0] if interval1[0] > interval2[0] else interval2[0]

    def prime_check_and_return(length: int) -> str:
        if length <= 0:
            return "NO"
        if is_prime(length):
            return "YES"
        return "NO"

    return prime_check_and_return(rightBound - leftBound)