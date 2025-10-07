import math

def prime_fib(n):
    def is_prime(p):
        if p < 2:
            return False
        limit = min(int(math.isqrt(p)) + 1, p)
        for k in range(2, limit):
            if p % k == 0:
                return False
        return True

    fib_sequence = [0, 1]

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        if is_prime(next_fib):
            n -= 1
            if n == 0:
                return next_fib