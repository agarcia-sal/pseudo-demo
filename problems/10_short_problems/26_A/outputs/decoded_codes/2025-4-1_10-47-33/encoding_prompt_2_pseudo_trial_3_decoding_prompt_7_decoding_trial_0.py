# Step 1: Input the number
total_count = int(input())  # Read an integer input for total count

# Step 2: Initialize a result counter
result = 0  # This will keep track of how many numbers have exactly two distinct prime factors

# Step 3: Loop through each number
for current_number in range(1, total_count + 1):
    distinct_prime_count = 0  # Counter for distinct prime factors
    temp_number = current_number  # Temporary variable to hold the current number

    # Step 4: Find prime factors
    for potential_factor in range(2, current_number):
        # Check if the potential factor is a divisor of temp_number
        if temp_number % potential_factor == 0:
            distinct_prime_count += 1  # Found a new distinct prime factor
            # Remove this prime factor completely from temp_number
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor  # Divide out the factor

    # Step 5: Count numbers with exactly two distinct primes
    if distinct_prime_count == 2:
        result += 1  # Increment result if exactly two distinct prime factors are found

# Step 6: Output the result
print(result)  # Print the final count of numbers with exactly two distinct prime factors
