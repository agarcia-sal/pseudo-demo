# Step 1: Read an integer input for the upper limit
upper_limit = int(input())

# Step 2: Initialize a variable to count the numbers with exactly two distinct prime factors
result_count = 0

# Step 3: Loop through each integer from 1 to upper_limit (inclusive)
for current_number in range(1, upper_limit + 1):
    # Initialize factor count for the current number
    distinct_prime_factor_count = 0
    # Temporary number to check for factors
    temp_number = current_number
    
    # Step 4: Check for factors starting from 2
    for potential_factor in range(2, current_number):
        # Check if potential_factor is a factor of temp_number
        if temp_number % potential_factor == 0:
            # Increment the count of distinct prime factors
            distinct_prime_factor_count += 1
            
            # Remove all occurrences of potential_factor from temp_number
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor

    # Step 5: If we found exactly 2 distinct prime factors, increment the result count
    if distinct_prime_factor_count == 2:
        result_count += 1

# Step 6: Output the final count of numbers with exactly two distinct prime factors
print(result_count)
