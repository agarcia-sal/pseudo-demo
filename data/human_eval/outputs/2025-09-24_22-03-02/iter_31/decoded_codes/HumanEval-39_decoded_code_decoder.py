import math

def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        limit = int(math.sqrt(p)) + 1
        upper_bound = p - 1
        if limit > upper_bound:
            limit = upper_bound
        for k in range(2, limit):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    while True:
        new_fib = f[-1] + f[-2]
        f.append(new_fib)
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]