# This program counts the number of prime numbers less than or equal to a given integer input.

# Function to count prime numbers up to upperLimit
def count_primes(upper_limit):
    # Initialize the counter for primes
    prime_count = 0

    # Loop through each number from 1 to upper_limit
    for current_number in range(1, upper_limit + 1):
        # Initialize a counter for factors of current_number
        factor_count = 0
        temp_number = current_number  # Temporary variable to manipulate current_number

        # Check for factors starting from 2 up to current_number - 1
        for potential_factor in range(2, current_number):
            # If current_number is divisible by potential_factor
            if temp_number % potential_factor == 0:
                factor_count += 1  # Found a new factor
                # While temp_number can still be divided by potential_factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor  # Remove all occurrences of factor

        # Determine if the current number is prime
        if factor_count == 1 and current_number > 1:  # Only 1 distinct factor (itself)
            prime_count += 1  # It is a prime number

    # Output the prime count
    print(prime_count)

# Accept input (using default input() function)
upper_limit = int(input())

# Call function to count primes
count_primes(upper_limit)
