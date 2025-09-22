def is_prime(n):
    if n <= 1:
        return False
    divisor_count = 0
    for j in range(2, n):
        if n % j == 0:
            divisor_count += 1
            # Remove all factors of j from n
            while n % j == 0:
                n //= j
    return divisor_count == 1

def count_primes(t):
    prime_count = 0
    for i in range(1, t + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count

# Input from user
t = int(input())
# Counting and printing the number of prime numbers up to t
print(count_primes(t))
