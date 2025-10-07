import math

def prime_fib(n):
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.isqrt(p)) + 1, p)):
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