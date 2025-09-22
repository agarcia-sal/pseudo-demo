# Step 1: Input integer value t
t = int(input())

# Step 2: Initialize the result variable
result = 0

# Step 3: Loop through numbers from 1 to t
for current_number in range(1, t + 1):
    # Step 3.1: Initialize factor_count
    factor_count = 0
    # Step 3.2: Set temp_number to current_number
    temp_number = current_number

    # Step 4: Check for factors
    for potential_factor in range(2, current_number):
        # Step 4.1: Check if temp_number is divisible by potential_factor
        if temp_number % potential_factor == 0:
            # Step 4.2: Increment factor_count
            factor_count += 1
            # Step 4.3: Remove all occurrences of potential_factor
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor

    # Step 5: Check if factor_count equals 2
    if factor_count == 2:
        # Step 5.1: Increment result
        result += 1

# Step 6: Output the result
print(result)
