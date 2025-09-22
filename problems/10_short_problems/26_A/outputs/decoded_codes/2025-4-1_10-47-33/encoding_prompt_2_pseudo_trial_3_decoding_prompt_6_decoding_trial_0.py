# Step 1: Input the number
total_count = int(input())  # Read an integer input

# Step 2: Initialize a result counter
result = 0  # This will count how many numbers have exactly two distinct prime factors

# Step 3: Loop through each number
for current_number in range(1, total_count + 1):
    distinct_prime_count = 0  # Counter for distinct prime factors
    temp_number = current_number  # Work with a copy of current_number

    # Step 4: Find prime factors
    for potential_factor in range(2, current_number):  # Check for prime factors
        if temp_number % potential_factor == 0:  # Check if it's divisible
            distinct_prime_count += 1  # Found a new distinct prime factor
            
            # Remove the factor completely from temp_number
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor
    
    # Step 5: Count numbers with exactly two distinct primes
    if distinct_prime_count == 2:
        result += 1  # Increment the result if we found exactly two distinct primes

# Step 6: Output the result
print(result)  # Print the total count of numbers with exactly two distinct prime factors
