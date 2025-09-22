# Step 1: Read an integer input called totalNumbers.
total_numbers = int(input())

# Step 2: Initialize a variable count_of_special_numbers to 0.
count_of_special_numbers = 0

# Step 3: Loop through each integer current_number from 1 to totalNumbers (inclusive)
for current_number in range(1, total_numbers + 1):
    # a. Initialize a variable divisor_count to 0.
    divisor_count = 0
    # b. Set current_value to current_number.
    current_value = current_number
    
    # Step 3c: Loop through each integer divisor from 2 to current_number - 1
    for divisor in range(2, current_number):
        # i. If current_value is divisible by divisor
        if current_value % divisor == 0:
            # Increment divisor_count by 1
            divisor_count += 1
            # While current_value is still divisible by divisor
            while current_value % divisor == 0:
                # Divide current_value by divisor
                current_value //= divisor
    
    # Step 3d: If divisor_count is equal to 2
    if divisor_count == 2:
        # Increment count_of_special_numbers by 1
        count_of_special_numbers += 1

# Step 4: After checking all numbers, print count_of_special_numbers.
print(count_of_special_numbers)

# Step 5: End
