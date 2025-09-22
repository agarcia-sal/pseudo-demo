# Get a non-negative integer input from the user
target_sum = abs(int(input()))

# Initialize a counter to keep track of the current index
current_index = 0

# Repeat indefinitely until the conditions are met
while True:
    # Calculate the sum of the first current_index integers
    current_sum = (current_index * (current_index + 1)) // 2  # Using integer division
    
    # Calculate the difference between current_sum and target_sum
    difference = current_sum - target_sum
    
    # Check if the current_sum equals the target_sum
    if current_sum == target_sum:
        print(current_index)  # Print the current index and exit
        break
    
    # Check if the current_sum is greater than the target_sum
    if current_sum > target_sum:
        # Check if the difference is even
        if difference % 2 == 0:
            print(current_index)  # Print the current index and exit
            break
    
    # Increment current_index by 1 for the next iteration
    current_index += 1
