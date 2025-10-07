import math

def prime_fib(n: int):
    def is_prime(p):
        if p < 2:
            return False
        upper_limit = min(int(math.isqrt(p)) + 1, p - 1)
        for k in range(2, upper_limit):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]