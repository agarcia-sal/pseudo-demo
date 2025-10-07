import math

def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        limit = int(math.sqrt(p)) + 1
        upper_bound = min(limit, p - 1)
        k = 2
        while k < upper_bound:
            if p % k == 0:
                return False
            k += 1
        return True

    f = [0, 1]
    while True:
        last_index = len(f) - 1
        second_last_index = len(f) - 2
        new_fib = f[last_index] + f[second_last_index]
        f.append(new_fib)
        if is_prime(f[last_index + 1]):
            n -= 1
        if n == 0:
            return f[last_index + 1]