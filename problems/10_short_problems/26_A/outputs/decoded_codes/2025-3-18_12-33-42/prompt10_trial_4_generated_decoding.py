def count_primes_up_to_t(t):
    """Count the number of prime numbers up to a given integer t."""
    prime_count = 0  # Initialize the count of prime numbers
    
    for i in range(1, t + 1):  # Loop through each integer from 1 to t
        factor_count = 0  # Initialize the count of divisors for the current number
        num = i  # The number to be checked for primality
        
        # Check for factors of num
        for j in range(2, i):  # Check divisors from 2 to i-1
            if num % j == 0:  # If j is a divisor of num
                factor_count += 1  # Increment the count of factors
                # Remove all occurrences of the factor
                while num % j == 0:
                    num //= j  # Divide num by j to remove the factor
        
        # Check if the current number i is prime
        if factor_count == 1:  # Exactly one factor (itself)
            prime_count += 1  # Increment the prime count

    return prime_count  # Return the total count of prime numbers found


# Read input from the user
t = int(input())  # User inputs a positive integer
result = count_primes_up_to_t(t)  # Call the function to count primes
print(result)  # Output the result
