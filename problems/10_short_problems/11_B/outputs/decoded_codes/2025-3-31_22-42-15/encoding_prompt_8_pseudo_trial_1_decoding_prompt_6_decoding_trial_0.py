# Obtain a positive integer from the user
target_value = abs(int(input()))  # Store the absolute value of the input in 'target_value'

# Initialize a variable 'current_index' to 0
current_index = 0

# Begin an infinite loop to calculate triangular numbers
while True:
    # Calculate the triangular number for 'current_index'
    triangular_number = (current_index * (current_index + 1)) // 2  # Using integer division

    # Calculate the difference between the triangular number and 'target_value'
    difference = triangular_number - target_value

    # Check if the triangular number equals the target_value
    if triangular_number == target_value:
        print(current_index)  # Print the current_index
        break  # Exit the loop

    # Check if the triangular number is greater than the target_value
    if triangular_number > target_value:
        # Check if the difference is an even number
        if difference % 2 == 0:  # If 'difference' is even
            print(current_index)  # Print the current_index
            break  # Exit the loop

    # Increment 'current_index' by 1 to check the next triangular number
    current_index += 1
