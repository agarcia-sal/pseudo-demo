import math

def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        upper_limit = min(int(math.sqrt(p)) + 1, p - 1)
        k = 2
        while k < upper_limit:
            if p % k == 0:
                return False
            k += 1
        return True

    f = [0, 1]
    while True:
        new_fib = f[-1] + f[-2]
        f.append(new_fib)
        current_fib = f[-1]
        if is_prime(current_fib):
            n -= 1
        if n == 0:
            return current_fib