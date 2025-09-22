# Step 1: Get input and calculate its absolute value
target_sum = abs(int(input()))

# Step 2: Initialize counter for consecutive integers
current_index = 0

# Step 3: Loop indefinitely to find the smallest integer
while True:
    # Step 3a: Calculate current sum of integers from 0 to current_index
    current_sum = current_index * (current_index + 1) // 2
    
    # Step 3b: Calculate the difference between current sum and target sum
    difference = current_sum - target_sum
    
    # Step 3c: Check for exact match
    if current_sum == target_sum:
        print(current_index)
        break
    
    # Step 3d: Check for overshoot
    if current_sum > target_sum:
        if difference % 2 == 0:
            print(current_index)
            break
    
    # Step 3e: Increment index for the next integer
    current_index += 1
