# Start the Program
total_count = int(input())  # Read an integer value from the user

# Initialize a Result Variable
count_of_numbers_with_two_distinct_prime_factors = 0  # This variable will hold the final count

# Loop Through Each Number
for current_number in range(1, total_count + 1):
    distinct_prime_factors_count = 0  # Count of distinct prime factors for the current number
    working_number = current_number  # Store original value of current_number

    # Check for Prime Factors
    for potential_factor in range(2, current_number):  # Check potential factors from 2 to current_number - 1
        if working_number % potential_factor == 0:  # If working_number is divisible by potential_factor
            distinct_prime_factors_count += 1  # Found a distinct prime factor
            # Remove all occurrences of this prime factor from working_number
            while working_number % potential_factor == 0:
                working_number //= potential_factor  # Divide working_number by potential_factor

    # Check for Two Distinct Factors
    if distinct_prime_factors_count == 2:  # If exactly two distinct prime factors are found
        count_of_numbers_with_two_distinct_prime_factors += 1  # Increment the count

# Output the Result
print(count_of_numbers_with_two_distinct_prime_factors)  # Print the final count
