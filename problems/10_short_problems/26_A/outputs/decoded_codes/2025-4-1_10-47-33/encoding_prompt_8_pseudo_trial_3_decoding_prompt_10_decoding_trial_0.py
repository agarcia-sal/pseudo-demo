def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(t):
    """Count the number of semiprime numbers from 1 to t."""
    semiprime_count = 0

    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        distinct_prime_count = 0
        current_number = i

        # Check for factors starting from 2
        for j in range(2, current_number + 1):
            if current_number % j == 0 and is_prime(j):
                distinct_prime_count += 1

                # Reduce current_number by all its occurrences of j
                while current_number % j == 0:
                    current_number //= j

            # Break early if we already found 3 distinct primes
            if distinct_prime_count > 2:
                break

        # If the number has exactly two distinct prime factors, it is a semiprime
        if distinct_prime_count == 2:
            semiprime_count += 1

    return semiprime_count

# Get the input value for t
t = int(input())

# Output the total count of semiprimes found
print(count_semiprimes(t))
