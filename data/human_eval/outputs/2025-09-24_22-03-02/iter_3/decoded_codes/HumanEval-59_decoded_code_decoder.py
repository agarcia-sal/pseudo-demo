def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True

    largest = 1
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            if is_prime(j):
                largest = max(largest, j)
            d = n // j
            if d != j and is_prime(d):
                largest = max(largest, d)
    return largest if largest != 1 else (n if is_prime(n) else 1)