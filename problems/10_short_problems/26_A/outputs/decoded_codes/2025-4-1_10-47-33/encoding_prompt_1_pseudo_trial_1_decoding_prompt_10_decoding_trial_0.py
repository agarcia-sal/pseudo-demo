def is_prime(n):
    """Check if the number n is a prime number."""
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

def count_primes(upper_limit):
    """Count the number of prime numbers up to a given upper limit."""
    prime_count = 0
    for i in range(1, upper_limit + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count

if __name__ == "__main__":
    upper_limit = int(input())
    total_primes = count_primes(upper_limit)
    print(total_primes)
