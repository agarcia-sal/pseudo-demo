from math import floor, sqrt
from typing import List

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        divisors: List[int] = [i for i in range(2, min(floor(sqrt(integer_p)) + 1, integer_p))]
        def check_divisibility(list_nums: List[int], integer_idx: int) -> bool:
            if integer_idx >= len(list_nums):
                return True
            if integer_p % list_nums[integer_idx] == 0:
                return False
            return check_divisibility(list_nums, integer_idx + 1)
        return check_divisibility(divisors, 0)

    linked_fib: List[int] = [0, 1]
    while True:
        new_value = linked_fib[-1] + linked_fib[-2]
        linked_fib.append(new_value)
        if is_prime(new_value):
            integer_n -= 1
            if integer_n == 0:
                return new_value