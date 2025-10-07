from typing import List


def count_up_to(n: int) -> List[int]:
    primes_list: List[int] = []

    def check_prime(k: int, d: int) -> bool:
        if d * d > k:
            return True
        if k % d == 0:
            return False
        return check_prime(k, d + 1)

    def loop_i(current: int) -> None:
        if not (current < n):
            return
        if check_prime(current, 2):
            primes_list.append(current)
        loop_i(current + 1)

    loop_i(2)
    return primes_list