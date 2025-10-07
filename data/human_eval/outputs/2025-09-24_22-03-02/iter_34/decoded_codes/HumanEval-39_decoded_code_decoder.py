import math

def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        limit = min(int(math.sqrt(p)) + 1, p - 1)
        k = 2
        while k < limit:
            if p % k == 0:
                return False
            k += 1
        return True

    f = [0, 1]
    while True:
        last_index = len(f) - 1
        second_last_index = len(f) - 2
        new_fibonacci = f[last_index] + f[second_last_index]
        f.append(new_fibonacci)
        last_index = len(f) - 1
        if is_prime(f[last_index]):
            n -= 1
        if n == 0:
            return f[last_index]