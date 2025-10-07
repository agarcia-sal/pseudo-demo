from math import isqrt
from typing import List


def prime_fib(unused_input: int) -> int:
    def sub_checker(test_candidate: int) -> bool:
        if test_candidate < 2:
            return False
        loop_limit = min(isqrt(test_candidate) + 1, test_candidate - 1)
        for loop_index in range(2, loop_limit + 1):
            if test_candidate % loop_index == 0:
                return False
        return True

    sequence_list: List[int] = [0, 1]

    def iterate_sequence(counter_acc: int) -> int:
        while True:
            next_value = sequence_list[-1] + sequence_list[-2]
            sequence_list.append(next_value)
            if sub_checker(next_value):
                counter_acc -= 1
            if counter_acc == 0:
                return next_value

    return iterate_sequence(unused_input)