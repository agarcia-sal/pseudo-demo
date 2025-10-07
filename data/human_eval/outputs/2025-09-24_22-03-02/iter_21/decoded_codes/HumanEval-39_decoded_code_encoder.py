import math

def prime_fib(n: int) -> int:
    def is_prime(p):
        if p < 2:
            return False
        limit = min(int(math.sqrt(p)) + 1, p - 1)
        for k in range(2, limit + 1):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    while True:
        new_fib = f[-1] + f[-2]
        f.append(new_fib)
        if is_prime(new_fib):
            n -= 1
        if n == 0:
            return new_fib