import math

def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        limit = int(math.sqrt(p)) + 1 if p > 1 else 0
        max_check = p - 1
        max_range = limit if limit < max_check else max_check
        for k in range(2, max_range):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    while True:
        last_index = len(f) - 1
        second_last_index = len(f) - 2
        new_fib = f[last_index] + f[second_last_index]
        f.append(new_fib)
        last_index = len(f) - 1
        last_fib = f[last_index]
        prime_check = is_prime(last_fib)
        if prime_check:
            n -= 1
        if n == 0:
            return last_fib