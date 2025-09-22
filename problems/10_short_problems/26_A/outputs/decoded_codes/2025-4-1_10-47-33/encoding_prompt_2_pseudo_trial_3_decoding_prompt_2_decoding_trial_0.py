# Step 1: Input the number
total_count = int(input())

# Step 2: Initialize a result counter
result = 0

# Step 3: Loop through each number
for current_number in range(1, total_count + 1):
    # Initialize distinct prime factor counter
    distinct_prime_count = 0
    temp_number = current_number  # Work with a copy of current_number

    # Step 4: Find prime factors
    for potential_factor in range(2, current_number):
        if temp_number % potential_factor == 0:  # Check divisibility
            distinct_prime_count += 1  # Increase distinct prime count
            # Remove all occurrences of this prime factor
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor

    # Step 5: Count numbers with exactly two distinct primes
    if distinct_prime_count == 2:
        result += 1

# Step 6: Output the result
print(result)
