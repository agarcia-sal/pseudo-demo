def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    largest = 1
    j = 2
    while j <= n:
        if n % j == 0 and is_prime(j):
            if largest < j:
                largest = j
        j += 1
    return largest