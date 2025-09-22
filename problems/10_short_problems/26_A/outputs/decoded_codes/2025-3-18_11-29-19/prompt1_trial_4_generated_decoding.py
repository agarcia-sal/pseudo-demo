# Step 1: Input an integer t
t = int(input())

# Step 2: Initialize the result variable
result = 0

# Step 3: Loop through each integer from 1 to t (inclusive)
for current_number in range(1, t + 1):
    # Initialize the distinct prime count
    distinct_prime_count = 0
    temp_number = current_number  # Set temp_number to current_number

    # Step 4: Find prime factors
    for potential_prime in range(2, current_number):  # Check potential prime factors
        if temp_number % potential_prime == 0:  # Check if divisible
            distinct_prime_count += 1  # Found a new distinct prime factor
            # Divide out all instances of potential_prime
            while temp_number % potential_prime == 0:
                temp_number //= potential_prime

    # Step 5: Check the distinct prime factor count
    if distinct_prime_count == 2:
        result += 1  # Increment result if exactly two distinct prime factors

# Step 6: Output the result
print(result)
