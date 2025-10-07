import math

def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        limit = min(int(math.isqrt(p)) + 1, p - 1)
        k = 2
        while k < limit:
            if p % k == 0:
                return False
            k += 1
        return True

    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]