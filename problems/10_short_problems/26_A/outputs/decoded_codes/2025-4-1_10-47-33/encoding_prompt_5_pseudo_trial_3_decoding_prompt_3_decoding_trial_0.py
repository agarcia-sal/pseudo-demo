def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(t):
    """Count how many numbers from 1 to t are semiprimes."""
    semiprime_count = 0  # Initialize a counter for semiprimes

    # Iterate through each number from 1 to t
    for current_number in range(2, t + 1):
        factor_count = 0    # Count of distinct prime factors
        temp_number = current_number  # Temporary variable to work with

        # Find prime factors
        for possible_prime in range(2, temp_number):
            if temp_number % possible_prime == 0 and is_prime(possible_prime):
                factor_count += 1  # Found a prime factor

                # Reduce temp_number by possible_prime
                while temp_number % possible_prime == 0:
                    temp_number //= possible_prime

        # Check if the current number is semiprime
        if factor_count == 2:
            semiprime_count += 1  # Increment counter for semiprimes

    return semiprime_count  # Return the total count of semiprimes

# Main execution flow
t = int(input())  # Get input from the user
result = count_semiprimes(t)  # Count semiprimes in the range
print(result)  # Output the result
