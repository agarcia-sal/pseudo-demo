# Start of the program

# Read an integer from the user and store the absolute value in target_sum
target_sum = abs(int(input()))

# Initialize the current index
current_index = 0

# Begin an infinite loop
while True:
    # Calculate the sum of the first current_index integers
    current_sum = (current_index * (current_index + 1)) // 2

    # Calculate the difference from the target sum
    difference_from_target = current_sum - target_sum

    # Check for an exact match
    if current_sum == target_sum:
        print(current_index)  # Output the value of current_index
        break  # Exit the loop

    # Check if current_sum exceeds target_sum
    if current_sum > target_sum:
        # Check if the difference from the target is even
        if difference_from_target % 2 == 0:
            print(current_index)  # Output the value of current_index
            break  # Exit the loop

    # Increment current_index by 1
    current_index += 1

# End of the program
