# Start of the program

# Step 2: Read an integer input 'time_period' 
time_period = int(input())

# Step 3: Initialize 'result_count' to 0
result_count = 0

# Step 4: For each integer 'current_number' from 1 to 'time_period' (inclusive)
for current_number in range(1, time_period + 1):
    # a. Initialize 'divisor_count' to 0
    divisor_count = 0
    # b. Set 'temp_number' to 'current_number'
    temp_number = current_number
    
    # c. For each integer 'potential_divisor' from 2 to 'current_number' - 1
    for potential_divisor in range(2, current_number):
        # i. If 'temp_number' is divisible by 'potential_divisor':
        if temp_number % potential_divisor == 0:
            # A. Increment 'divisor_count' by 1
            divisor_count += 1
            
            # B. While 'temp_number' is divisible by 'potential_divisor':
            while temp_number % potential_divisor == 0:
                # I. Divide 'temp_number' by 'potential_divisor'
                temp_number //= potential_divisor
    
    # d. If 'divisor_count' equals 2:
    if divisor_count == 2:
        # i. Increment 'result_count' by 1
        result_count += 1

# Step 5: Print 'result_count'
print(result_count)

# End of the program
