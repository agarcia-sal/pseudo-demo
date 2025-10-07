from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisor(integer_k: int) -> bool:
            limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
            if integer_k > limit:
                return True
            if integer_p % integer_k == 0:
                return False
            return check_divisor(integer_k + 1)

        return check_divisor(2)

    seq_fibo: List[int] = [0, 1]

    def loop_fib(counter_n: int, seq_fibo_inner: List[int]) -> int:
        if counter_n == 0:
            return seq_fibo_inner[-1]
        next_val = seq_fibo_inner[-1] + seq_fibo_inner[-2]
        seq_new = seq_fibo_inner + [next_val]
        if is_prime(next_val):
            return loop_fib(counter_n - 1, seq_new)
        return loop_fib(counter_n, seq_new)

    return loop_fib(integer_n, seq_fibo)