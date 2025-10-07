def largest_prime_factor(n):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            if j > largest:
                largest = j
    return largest