import math

def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        limit = int(math.sqrt(p)) + 1
        limit = min(limit, p - 1)
        for k in range(2, limit):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    while True:
        length = len(f)
        last = f[length - 1]
        second_last = f[length - 2]
        next_fib = last + second_last
        f.append(next_fib)
        length += 1
        if is_prime(f[length - 1]):
            n -= 1
        if n == 0:
            return f[length - 1]