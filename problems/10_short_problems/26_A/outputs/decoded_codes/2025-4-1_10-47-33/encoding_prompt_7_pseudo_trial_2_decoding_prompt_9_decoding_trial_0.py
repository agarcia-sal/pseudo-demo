def count_semi_primes(t):
    total_semi_primes = 0  # Initialize count of semi-prime numbers

    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        divisor_count = 0  # Count of distinct prime factors
        current_number = i  # Store the current number to work with

        # Check for divisors from 2 up to (i-1)
        for j in range(2, i):
            if current_number % j == 0:  # If j is a divisor of current_number
                divisor_count += 1  # Increment the distinct prime factor count
                
                # Divide current number by j until it is no longer divisible
                while current_number % j == 0:
                    current_number //= j

        # Check if the number has exactly two distinct prime factors
        if divisor_count == 2:
            total_semi_primes += 1  # Increment count of semi-primes

    return total_semi_primes  # Return the total number of semi-primes
