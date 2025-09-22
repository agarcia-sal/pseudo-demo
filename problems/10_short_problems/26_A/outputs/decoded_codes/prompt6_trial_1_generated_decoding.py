# Read an integer input from user input
input_value = int(input())

# Initialize a variable to store the count of numbers with exactly two distinct prime factors
result_count = 0

# Loop through all integers from 1 to input_value (inclusive)
for current_number in range(1, input_value + 1):
    # Initialize a counter for distinct prime factors
    distinct_prime_count = 0
    remaining_value = current_number

    # Check for potential prime factors from 2 up to current_number-1
    for potential_prime_factor in range(2, current_number):
        # If potential_prime_factor is a divisor of remaining_value
        if remaining_value % potential_prime_factor == 0:
            # We found a valid prime factor, increment the counter
            distinct_prime_count += 1

            # Divide remaining_value by potential_prime_factor until it no longer divides evenly
            while remaining_value % potential_prime_factor == 0:
                remaining_value //= potential_prime_factor

    # Check if we found exactly two distinct prime factors
    if distinct_prime_count == 2:
        # If yes, increment the result counter
        result_count += 1

# Output the total count of numbers with exactly two distinct prime factors
print(result_count)
