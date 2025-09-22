# Step 1: Read input and take the absolute value
target_value = abs(int(input()))

# Step 2: Initialize index variable
index = 0

# Step 3: Loop until a condition is met
while True:
    # Calculate currentSum using the formula for the sum of the first 'index' integers
    current_sum = (index * (index + 1)) // 2
    
    # Compute the difference between currentSum and targetValue
    difference = current_sum - target_value
    
    # Check if currentSum is equal to targetValue
    if current_sum == target_value:
        print(index)  # Print index and stop the loop
        break
    
    # Check if currentSum is greater than targetValue
    if current_sum > target_value:
        # Check if difference is an even number
        if difference % 2 == 0:
            print(index)  # Print index and stop the loop
            break
    
    # Increment index by 1 for the next iteration
    index += 1
