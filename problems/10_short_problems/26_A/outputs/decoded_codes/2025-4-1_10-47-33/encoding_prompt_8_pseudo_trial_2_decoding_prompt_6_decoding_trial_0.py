# Read an integer value from user input
limit = int(input())

# Initialize a variable to keep track of the number of semiprimes found
semiprime_count = 0

# Loop through each number from 1 to the limit (inclusive)
for current_number in range(1, limit + 1):
    # Initialize a count for prime factors of the current number
    prime_factor_count = 0
    # Set temp_number to current_number for factorization
    temp_number = current_number

    # Check for potential factors starting from 2 up to current_number (exclusive)
    for potential_factor in range(2, current_number):
        # If temp_number is divisible by potential_factor
        if temp_number % potential_factor == 0:
            # Increment the prime factor count
            prime_factor_count += 1
            
            # Divide temp_number by potential_factor until it's no longer divisible
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor

    # If the number has exactly 2 prime factors, it's a semiprime
    if prime_factor_count == 2:
        semiprime_count += 1  # Increment the semiprime count

# Output the total number of semiprime numbers found
print(semiprime_count)
