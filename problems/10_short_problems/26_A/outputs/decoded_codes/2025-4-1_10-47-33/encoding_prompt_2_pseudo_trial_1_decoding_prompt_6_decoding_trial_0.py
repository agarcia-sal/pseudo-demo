# Step 1: Read an integer input value, t
upper_limit = int(input())  # this will be our 't'

# Step 2: Initialize a variable to count the suitable integers
result_count = 0  # this will be our 'resultCount'

# Step 3: Iterate through each integer from 1 to upper_limit
for current_number in range(1, upper_limit + 1):
    factor_count = 0  # initialize the factor count for the current number
    current_value = current_number  # use current_number for factorization

    # Step 4: Check for factors starting from 2 up to one less than current_number
    for potential_factor in range(2, current_number):
        if current_value % potential_factor == 0:  # is potential_factor a factor?
            factor_count += 1  # we found a new factor
            # Divide out all instances of this factor
            while current_value % potential_factor == 0:
                current_value //= potential_factor

    # Step 5: Check if the current_number has exactly two distinct prime factors
    if factor_count == 2:
        result_count += 1  # count this current_number

# Step 6: Output the total count of integers with exactly two distinct prime factors
print(result_count)
