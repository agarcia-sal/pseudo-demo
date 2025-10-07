from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisor(integer_k: int) -> bool:
            limit = min(integer_p - 1, floor(sqrt(integer_p)) + 1)
            if integer_k >= limit:
                return True
            if integer_p % integer_k == 0:
                return False
            return check_divisor(integer_k + 1)

        return check_divisor(2)

    list_fibonacci: List[int] = [0, 1]

    def generate_next(list_fib: List[int]) -> List[int]:
        new_value = list_fib[-1] + list_fib[-2]
        return list_fib + [new_value]

    while integer_n != 0:
        list_fibonacci = generate_next(list_fibonacci)
        if is_prime(list_fibonacci[-1]):
            integer_n -= 1

    return list_fibonacci[-1]