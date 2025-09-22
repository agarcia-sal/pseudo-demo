# Start the program

# Receive input
total_numbers = int(input())  # Get an integer value from the user

# Initialize a counter
semiprime_count = 0  # To track the number of semiprimes found

# Iterate through numbers
for current_number in range(1, total_numbers + 1):
    prime_factor_count = 0  # Count of prime factors
    temp_number = current_number  # Make a copy of current_number

    # Check for prime factors
    for potential_prime in range(2, current_number):
        if temp_number % potential_prime == 0:  # Check if divisible
            prime_factor_count += 1  # Found a prime factor
            # Remove all occurrences of that prime factor
            while temp_number % potential_prime == 0:
                temp_number //= potential_prime  

    # Determine semiprime status
    if prime_factor_count == 2:  # Exactly two prime factors
        semiprime_count += 1  # Increment semiprime count

# Output the result
print(semiprime_count)  # Total number of semiprime numbers found

# End the program
