from typing import Union

def largest_prime_factor(input_number: int) -> int:
    def is_prime(candidate: int) -> bool:
        if candidate < 2:
            return False
        for divisor in range(2, int(candidate ** 0.5) + 1):
            if candidate % divisor == 0:
                return False
        return True

    largest_factor: int = 1
    for current_divisor in range(2, input_number + 1):
        if input_number % current_divisor == 0 and is_prime(current_divisor):
            if current_divisor > largest_factor:
                largest_factor = current_divisor
    return largest_factor