# Step 1: Receive an integer input from the user and take its absolute value
target_number = abs(int(input()))

# Step 2: Initialize a counter variable, current_index, to 0
current_index = 0

# Step 3: Enter an infinite loop to perform calculations
while True:
    # Step 4: Calculate the sum of integers from 0 to current_index
    sum_value = (current_index * (current_index + 1)) // 2
    
    # Step 5: Determine the difference between sum_value and target_number
    difference_from_target = sum_value - target_number
    
    # Step 6: Check if sum_value is equal to target_number
    if sum_value == target_number:
        print(current_index)  # Print current_index if condition is met
        break  # Exit the loop
    
    # Step 7: Check if sum_value is greater than target_number
    if sum_value > target_number:
        # If difference_from_target is even
        if difference_from_target % 2 == 0:
            print(current_index)  # Print current_index if condition is met
            break  # Exit the loop
            
    # Step 8: Increment current_index by 1
    current_index += 1
