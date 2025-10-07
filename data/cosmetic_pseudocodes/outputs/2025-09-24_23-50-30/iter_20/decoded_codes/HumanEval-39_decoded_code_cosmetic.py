from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        for integer_z in range(2, limit + 1):
            if integer_p % integer_z == 0:
                return False
        return True

    collection_seq: List[int] = [0, 1]

    while True:
        integer_a = collection_seq[-1]
        integer_b = collection_seq[-2]
        integer_c = integer_a + integer_b
        collection_seq.append(integer_c)
        if is_prime(integer_c):
            integer_n -= 1
            if integer_n == 0:
                return integer_c