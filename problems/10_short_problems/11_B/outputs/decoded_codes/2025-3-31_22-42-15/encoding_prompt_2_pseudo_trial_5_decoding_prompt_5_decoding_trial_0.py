# Read the integer input from the user and store its absolute value
target_sum = abs(int(input()))

# Initialize a counter to keep track of the current index
current_index = 0

# Begin an infinite loop
while True:
    # Calculate the sum of the first `current_index` integers
    sum_of_series = (current_index * (current_index + 1)) // 2
    
    # Determine the difference between the calculated sum and target sum
    difference = sum_of_series - target_sum
    
    # Check if sum_of_series equals target_sum
    if sum_of_series == target_sum:
        print(current_index)
        break  # Stop the loop if condition is met
    
    # Check if sum_of_series is greater than target_sum
    if sum_of_series > target_sum:
        # Check if the difference is even
        if difference % 2 == 0:
            print(current_index)
            break  # Stop the loop if condition is met
    
    # Increment the counter for the next iteration
    current_index += 1
