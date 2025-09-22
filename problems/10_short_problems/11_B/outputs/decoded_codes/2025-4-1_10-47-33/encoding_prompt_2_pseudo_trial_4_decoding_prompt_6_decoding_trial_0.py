# Step 1: Read an integer input from the user and store the absolute value in target_sum
target_sum = abs(int(input()))

# Step 2: Initialize current_index to 0
current_index = 0

# Step 3: Start an infinite loop
while True:
    # Step 4: Calculate current_sum using the formula for the sum of the first current_index integers
    current_sum = (current_index * (current_index + 1)) // 2
    
    # Step 5: Calculate the difference from the target
    difference_from_target = current_sum - target_sum
    
    # Step 6: Check for exact match
    if current_sum == target_sum:
        print(current_index)  # Output the value of current_index
        break  # Exit the loop

    # Step 7: Check if current_sum exceeds target_sum
    if current_sum > target_sum:
        # Check if the difference is even
        if difference_from_target % 2 == 0:
            print(current_index)  # Output the value of current_index
            break  # Exit the loop

    # Step 8: Increment current_index by 1
    current_index += 1
