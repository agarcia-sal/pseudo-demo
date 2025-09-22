# Read an integer input from the user and store its absolute value in target_sum
target_sum = abs(int(input()))

# Initialize a counter to keep track of the current index
current_index = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first current_index integers using the formula for the sum of a series
    sum_of_series = (current_index * (current_index + 1)) // 2
    
    # Compute the difference between the sum and the target sum
    difference = sum_of_series - target_sum
    
    # Check if the sum matches the target sum
    if sum_of_series == target_sum:
        print(current_index)  # Output the current index
        break  # Exit the loop
    
    # Check if the sum exceeds the target sum
    if sum_of_series > target_sum:
        # Check if the difference is even
        if difference % 2 == 0:
            print(current_index)  # Output the current index
            break  # Exit the loop
    
    # Increment the counter for the next iteration
    current_index += 1
