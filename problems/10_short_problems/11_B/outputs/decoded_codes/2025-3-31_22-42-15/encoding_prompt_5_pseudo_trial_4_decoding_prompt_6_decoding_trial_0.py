# Start the program

# Get user input and store the absolute value of the entered number
target_value = abs(int(input()))

# Initialize a counter to 0
counter = 0

# Begin an endless loop to find the triangular number
while True:
    # Calculate the triangular number using the formula
    triangular_number = (counter * (counter + 1)) // 2
    
    # Calculate the difference from the target value
    difference = triangular_number - target_value
    
    # Check if the triangular number equals the target value
    if triangular_number == target_value:
        # Print the counter as we found a match
        print(counter)
        break  # Exit the loop

    # Check if the triangular number is greater than the target value
    elif triangular_number > target_value:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # Print the counter as a different condition has been met
            print(counter)
            break  # Exit the loop

    # Increment the counter by 1 for the next iteration
    counter += 1

# End of the program
