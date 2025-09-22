# Read an integer value from input, representing the upper limit
upper_limit = int(input())

# Initialize a counter to keep track of numbers with exactly two distinct prime factors
count_of_numbers_with_two_prime_factors = 0

# Loop through each number from 1 to upper_limit
for current_number in range(1, upper_limit + 1):
    
    # Initialize a counter for distinct prime factors
    distinct_prime_factor_count = 0
    remaining_number = current_number

    # Check for factors from 2 up to the current number (inclusive)
    for potential_prime_factor in range(2, current_number + 1):
        # If potential_prime_factor is a divisor of remaining_number
        if remaining_number % potential_prime_factor == 0:
            
            # Increment the count of distinct prime factors
            distinct_prime_factor_count += 1
            
            # Divide remaining_number by potential_prime_factor until it no longer is divisible
            while remaining_number % potential_prime_factor == 0:
                remaining_number //= potential_prime_factor

        # If we have found 2 distinct prime factors, we can break out of the loop early
        if distinct_prime_factor_count == 2:
            break

    # If exactly two distinct prime factors were found, increment the total counter
    if distinct_prime_factor_count == 2:
        count_of_numbers_with_two_prime_factors += 1

# Output the total count of numbers with exactly two distinct prime factors
print(count_of_numbers_with_two_prime_factors)
