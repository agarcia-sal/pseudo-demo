from typing import List

def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def check_divisor(d: int) -> bool:
            if d >= n:
                return True
            if n % d == 0:
                return False
            return check_divisor(d + 1)
        if n < 2:
            return False
        return check_divisor(2)

    primes: List[int] = []
    x: int = 100
    y: int = 2
    while y <= x:
        if is_prime(y):
            primes.append(y)
        y += 1

    def find_combination(index1: int, index2: int, index3: int) -> bool:
        length = len(primes)
        if index1 >= length:
            return False
        if index2 >= length:
            return find_combination(index1 + 1, 0, 0)
        if index3 >= length:
            return find_combination(index1, index2 + 1, 0)
        if primes[index1] * primes[index2] * primes[index3] == a:
            return True
        return find_combination(index1, index2, index3 + 1)

    return find_combination(0, 0, 0)