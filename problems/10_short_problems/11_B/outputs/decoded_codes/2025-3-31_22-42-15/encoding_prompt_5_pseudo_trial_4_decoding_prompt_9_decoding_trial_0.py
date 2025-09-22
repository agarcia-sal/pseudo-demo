# Start the program

# Get user input
target_value = abs(int(input()))  # Store the absolute value of the entered number

# Initialize a counter
counter = 0

# Begin an endless loop to find the triangular number
while True:
    # Calculate the triangular number using the formula: triangularNumber = (counter * (counter + 1)) / 2
    triangular_number = (counter * (counter + 1)) // 2
    
    # Calculate the difference
    difference = triangular_number - target_value
    
    # Check if the triangular number matches the target value
    if triangular_number == target_value:
        print(counter)  # Print the counter (match found)
        break  # Exit the loop

    # Check if the triangular number exceeds the target value
    elif triangular_number > target_value:
        # If the difference is an even number
        if difference % 2 == 0:
            print(counter)  # Print the counter (different condition met)
            break  # Exit the loop

    # Increment the counter by 1 (move to the next counter value)
    counter += 1

# End the program
