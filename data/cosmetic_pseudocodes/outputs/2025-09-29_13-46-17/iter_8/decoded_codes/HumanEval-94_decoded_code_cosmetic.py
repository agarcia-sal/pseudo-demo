from math import sqrt, floor
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    rando_scalar: int = 0  # unused, preserved as in pseudocode

    def isPrime(integer_value: int) -> bool:
        def helper_crisp(k: int, limit: int) -> bool:
            if k >= limit:
                return True
            if integer_value % k != 0:
                return helper_crisp(k + 1, limit)
            return False

        if integer_value < 2:
            return False
        return helper_crisp(2, floor(sqrt(integer_value)) + 1)

    def accumulate_digits(n: int, acc: int) -> int:
        if n == 0:
            return acc
        return accumulate_digits(n // 10, acc + (n % 10))

    def search(lst: List[int], ct: int, cur_max: int) -> int:
        if ct == len(lst):
            return cur_max
        h = lst[ct]
        nxt_max = h if (h > cur_max and isPrime(h)) else cur_max
        return search(lst, ct + 1, nxt_max)

    chosen_prime = search(list_of_integers, 0, 0)
    return accumulate_digits(chosen_prime, 0)