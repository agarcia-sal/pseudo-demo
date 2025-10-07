from typing import Callable

def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for m in range(2, k):
            if k % m == 0:
                return False
        return True

    max_factor: int = 1
    counter: int = 2
    while counter <= n:
        if n % counter == 0:
            if is_prime(counter) and counter > max_factor:
                max_factor = counter
        counter += 1
    return max_factor