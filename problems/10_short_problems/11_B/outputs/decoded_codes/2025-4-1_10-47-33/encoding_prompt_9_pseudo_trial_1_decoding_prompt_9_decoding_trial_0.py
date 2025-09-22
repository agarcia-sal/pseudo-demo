# Get Input from the user and convert it to absolute value
target_sum = abs(int(input()))

# Initialize Counter
current_index = 0

# Loop indefinitely
while True:
    # Calculate Sum using the formula for the sum of the first n integers
    current_sum = current_index * (current_index + 1) // 2
    
    # Calculate the difference between current sum and target sum
    difference = current_sum - target_sum
    
    # Check for Exact Match
    if current_sum == target_sum:
        print(current_index)
        break  # Terminate the loop
    
    # Check for Overshoot
    if current_sum > target_sum:
        if difference % 2 == 0:  # Check if difference is even
            print(current_index)
            break  # Terminate the loop
    
    # Increment Index for the next iteration
    current_index += 1
