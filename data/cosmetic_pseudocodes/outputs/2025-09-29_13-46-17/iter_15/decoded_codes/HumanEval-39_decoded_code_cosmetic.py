from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        def check_divisor(d: int) -> bool:
            if d > isqrt(integer_p) + 1 or d >= integer_p:
                return True
            if integer_p % d == 0:
                return False
            return check_divisor(d + 1)

        if integer_p < 2:
            return False
        return check_divisor(2)

    def next_fib_term(seq: List[int]) -> int:
        return seq[-1] + seq[-2]

    def prime_fib_loop(seq: List[int], count: int) -> int:
        if count == 0:
            return seq[-1]
        new_seq = seq + [next_fib_term(seq)]
        if is_prime(new_seq[-1]):
            return prime_fib_loop(new_seq, count - 1)
        return prime_fib_loop(new_seq, count)

    return prime_fib_loop([0, 1], integer_n)