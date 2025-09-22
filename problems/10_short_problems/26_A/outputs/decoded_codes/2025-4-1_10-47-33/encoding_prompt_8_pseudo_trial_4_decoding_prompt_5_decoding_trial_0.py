# Start Program

# Step 2: Get Input
total_numbers = int(input())

# Step 3: Initialize Count
result = 0  # This will keep track of numbers that are products of exactly two primes

# Step 4: Iterate Through Numbers
for current_number in range(1, total_numbers + 1):
    prime_factor_count = 0  # Count of distinct prime factors
    temp_number = current_number  # Work with a copy of current_number

    # Step 5: Check for Prime Factors
    for potential_factor in range(2, current_number):
        if temp_number % potential_factor == 0:  # Check if potential_factor divides temp_number
            prime_factor_count += 1  # Found a new prime factor
            while temp_number % potential_factor == 0:  # Remove all occurrences of this factor
                temp_number //= potential_factor

    # Step 6: Evaluate Condition
    if prime_factor_count == 2:  # Check if there are exactly 2 distinct prime factors
        result += 1  # Found a valid number

# Step 7: Output the Result
print(result)  # Print the total count of numbers that are products of exactly two primes

# End Program
