# Step 1: Read input value
upper_limit = int(input())  # integer t from user

# Step 2: Initialize result counter
total_count = 0  # Variable to count numbers with exactly two distinct prime factors

# Step 3: Loop through each number from 1 to upper_limit
for current_number in range(1, upper_limit + 1):
    distinct_prime_count = 0  # Count of distinct prime factors for current_number
    current_value = current_number  # Value to factorize
    
    # Step 4: Find prime factors
    for potential_prime in range(2, current_number):  # Check potential prime factors
        if current_value % potential_prime == 0:  # Check divisibility
            distinct_prime_count += 1  # Found a new distinct prime factor
            # Divide out all instances of potential_prime
            while current_value % potential_prime == 0:
                current_value //= potential_prime

    # Step 5: Check if there are exactly two distinct prime factors
    if distinct_prime_count == 2:
        total_count += 1  # Increment the count if there are exactly two distinct primes

# Step 6: Output the result
print(total_count)  # Print the total count of numbers with exactly two distinct prime factors
