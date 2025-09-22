# Step 1: Read an integer input value t which represents the upper limit for checking numbers.
t = int(input())

# Step 2: Initialize a variable result_count to 0 to keep track of how many numbers have exactly two distinct prime factors.
result_count = 0

# Step 3: Loop through each number from 1 to t
for current_number in range(1, t + 1):
    # Initialize a variable distinct_prime_factors_count to 0
    distinct_prime_factors_count = 0
    # Set temp_number to current_number
    temp_number = current_number
    
    # Step 4: Check for potential prime factors starting from 2
    for potential_factor in range(2, current_number):
        # Check if temp_number is divisible by potential_factor
        if temp_number % potential_factor == 0:
            # Increment the distinct prime factors count
            distinct_prime_factors_count += 1
            # While temp_number is divisible by potential_factor
            while temp_number % potential_factor == 0:
                # Divide temp_number by potential_factor
                temp_number //= potential_factor
    
    # Step 5: After checking all potential factors
    if distinct_prime_factors_count == 2:
        # Increment result_count if there are exactly two distinct prime factors
        result_count += 1

# Step 6: Output the value of result_count
print(result_count)
