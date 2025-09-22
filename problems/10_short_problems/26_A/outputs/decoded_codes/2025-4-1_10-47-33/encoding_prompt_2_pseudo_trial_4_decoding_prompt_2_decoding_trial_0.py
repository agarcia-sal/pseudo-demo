# Step 1: Input
t = int(input())  # Read an integer value `t`

# Step 2: Initialize
result = 0  # This will hold the count of specific numbers

# Step 3: Loop through numbers
for current_number in range(1, t + 1):
    # Initialize the number of distinct prime factors
    factor_count = 0
    temp_number = current_number  # Set a variable `temp_number` equal to `current_number`

    # Step 4: Check for factors
    for potential_factor in range(2, current_number):  # Start from 2 to one less than current_number
        if temp_number % potential_factor == 0:  # Check if `potential_factor` is a factor
            factor_count += 1  # Found a new distinct prime factor
            # While loop to remove all occurrences of `potential_factor`
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor 

    # Step 5: Count primes
    if factor_count == 2:  # Exactly two distinct prime factors
        result += 1  # Increment the result

# Step 6: Output
print(result)  # Output the total count of numbers with exactly two distinct prime factors
