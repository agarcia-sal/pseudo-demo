from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        for q in range(2, m):
            if m % q == 0:
                return False
        return True

    result: int = 1
    candidate: int = 2
    while candidate <= n:
        if n % candidate == 0:
            if is_prime(candidate):
                # update result to the max of result and candidate without using max()
                result = (result + candidate + abs(result - candidate)) // 2
        candidate += 1
    return result