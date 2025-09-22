def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(t):
    """Count how many semiprime numbers are between 1 and t (inclusive)."""
    semiprime_count = 0  # Initialize a counter for semiprimes

    # Iterate through each number from 1 to t
    for current_number in range(1, t + 1):
        factor_count = 0  # This will count distinct prime factors
        temp_number = current_number  # A temporary copy to factorize

        # Find prime factors of the current number
        for possible_prime in range(2, current_number):
            if temp_number % possible_prime == 0:  # Check if possible_prime is a factor
                factor_count += 1  # Found a new prime factor

                # Reduce temp_number by this prime factor
                while temp_number % possible_prime == 0:
                    temp_number //= possible_prime  # Divide by possible_prime

        # Check for semiprime condition
        if factor_count == 2:  # Exactly two distinct prime factors
            semiprime_count += 1  # Increment the semiprime count

    return semiprime_count  # Return the total count of semiprimes

# Input for the range to check semiprimes
t = int(input())  # Get the upper limit from user input

# Call the function to count semiprimes and print the result
result = count_semiprimes(t)
print(result)  # Output the number of semiprimes found
