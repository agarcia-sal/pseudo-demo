def prime_fib(n):
    def is_prime(p):
        if p < 2:
            return False
        limit = min(int(p**0.5) + 1, p - 1)
        for k in range(2, limit):
            if p % k == 0:
                return False
        return True

    fibonacci_sequence = [0, 1]
    while True:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        if is_prime(fibonacci_sequence[-1]):
            n -= 1
        if n == 0:
            return fibonacci_sequence[-1]