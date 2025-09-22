def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semiprimes(t):
    """Count the number of semiprime numbers from 1 to t."""
    semiprime_count = 0  # Initialize semiprime count

    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        distinct_prime_count = 0  # Count of distinct prime factors
        current_number = i  # Make a copy of the current number for manipulation

        # Check for factors starting from 2
        for j in range(2, i):
            if current_number % j == 0:  # If j is a divisor of current_number
                distinct_prime_count += 1  # Found a new distinct prime factor

                # Divide current_number by j until it no longer divides evenly
                while current_number % j == 0:
                    current_number //= j

        # If exactly two distinct prime factors are found, it is a semiprime
        if distinct_prime_count == 2:
            semiprime_count += 1  # Increment semiprime count

    return semiprime_count  # Return the total count of semiprimes

# Main execution
if __name__ == "__main__":
    t = int(input())  # Get the upper limit number
    result = count_semiprimes(t)  # Count semiprimes
    print(result)  # Output the total count of semiprimes
