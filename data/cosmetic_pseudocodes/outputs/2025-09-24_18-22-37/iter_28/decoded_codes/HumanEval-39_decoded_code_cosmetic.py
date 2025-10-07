from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        flag_not_prime: bool = False
        if integer_p < 2:
            flag_not_prime = True
        else:
            limit_m: int = min(int(sqrt(integer_p)) + 1, integer_p - 1)
            iterator_j: int = 2
            while iterator_j <= limit_m and not flag_not_prime:
                if integer_p % iterator_j == 0:
                    flag_not_prime = True
                else:
                    pass  # no operation
                iterator_j += 1

        if flag_not_prime:
            return False
        else:
            return True

    fib_sequence: List[int] = [0, 1]
    continue_flag: bool = True
    while continue_flag:
        second_last_index: int = len(fib_sequence) - 2
        last_index: int = len(fib_sequence) - 1
        penultimate_value: int = fib_sequence[second_last_index]
        last_value: int = fib_sequence[last_index]
        next_fib: int = penultimate_value + last_value
        fib_sequence.append(next_fib)

        if is_prime(fib_sequence[-1]):
            integer_n -= 1

        if integer_n == 0:
            continue_flag = False

    return fib_sequence[-1]