from typing import List


def prime_length(input_string: str) -> bool:
    n: int = len(input_string)
    if n <= 1:
        return False
    divisors: List[int] = [x for x in range(n - 1, 1, -1)]

    def check_divisor(i: int) -> bool:
        if i < 0:
            return True
        if n % divisors[i] == 0:
            return False
        return check_divisor(i - 1)

    return check_divisor(len(divisors) - 1)