from math import sqrt, floor
from typing import List

def prime_fib(magnitude_alpha: int) -> int:
    def is_prime(magnitude_beta: int) -> bool:
        if magnitude_beta < 2:
            return False
        magnitude_delta = min(floor(sqrt(magnitude_beta)) + 1, magnitude_beta - 1)
        magnitude_gamma = 2
        while magnitude_gamma <= magnitude_delta:
            if magnitude_beta % magnitude_gamma == 0:
                return False
            magnitude_gamma += 1
        return True

    sequence_omega: List[int] = [0, 1]

    while True:
        temp_sum = sequence_omega[-1] + sequence_omega[-2]
        sequence_omega.append(temp_sum)

        if is_prime(sequence_omega[-1]):
            magnitude_alpha -= 1

        if magnitude_alpha == 0:
            return sequence_omega[-1]