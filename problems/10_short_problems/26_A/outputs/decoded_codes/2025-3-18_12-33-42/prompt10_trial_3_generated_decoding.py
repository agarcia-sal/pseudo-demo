def count_primes(t):
    """
    Count the number of prime numbers up to a given limit.

    Parameters:
    t (int): The upper limit for checking prime numbers.

    Returns:
    int: The count of prime numbers less than or equal to t.
    """
    # Initialize the result counter
    prime_count = 0

    # Iterate from 2 to t (inclusive)
    for i in range(2, t + 1):
        factor_count = 0  # Counter for factors of i
        num = i           # Temporary variable for factorization

        # Find factors of i
        for j in range(2, i):
            if num % j == 0:  # Check if j is a factor of num
                factor_count += 1  # Increment the factor count
                while num % j == 0:
                    num //= j  # Factor out j from num

        # Check if i is prime
        if factor_count == 1:  # A prime number has exactly one distinct factor: itself
            prime_count += 1  # Increment the prime count

    return prime_count


# Input from user
t = int(input())
# Call the function and print the result
result = count_primes(t)
print(result)
