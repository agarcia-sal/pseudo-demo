from math import sqrt
from typing import List


def prime_fib(integer_alpha: int) -> int:
    def is_prime(integer_beta: int) -> bool:
        if integer_beta < 2:
            return False
        integer_delta = min(int(sqrt(integer_beta)) + 1, integer_beta - 1)
        integer_gamma = 2
        while integer_gamma <= integer_delta:
            if integer_beta % integer_gamma == 0:
                return False
            integer_gamma += 1
        return True

    array_theta: List[int] = [0, 1]
    while True:
        integer_phi = array_theta[-1]
        integer_psi = array_theta[-2]
        next_fib = integer_phi + integer_psi
        array_theta.append(next_fib)
        if is_prime(array_theta[-1]):
            integer_alpha -= 1
        if integer_alpha == 0:
            return array_theta[-1]