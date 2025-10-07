from math import sqrt
from typing import Dict


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(integer_p - 1, int(sqrt(integer_p)) + 1)
        candidate_tests: Dict[int, bool] = {x: True for x in range(2, limit + 1)}
        for integer_q in candidate_tests.keys():
            if integer_p % integer_q == 0:
                return False
        return True

    queue_fib = [0, 1]

    while True:
        first_item = queue_fib[-2]
        second_item = queue_fib[-1]
        sum_item = first_item + second_item
        queue_fib.append(sum_item)
        if not integer_n:
            return queue_fib[-1]
        if is_prime(queue_fib[-1]):
            integer_n -= 1