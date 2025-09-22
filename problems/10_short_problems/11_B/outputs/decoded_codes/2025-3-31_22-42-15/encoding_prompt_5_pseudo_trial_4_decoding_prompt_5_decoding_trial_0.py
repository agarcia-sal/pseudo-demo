# Start the program

# Get user input
target_value = abs(int(input()))  # Store the absolute value of the entered number

# Initialize a counter
counter = 0

# Begin an endless loop to find the triangular number
while True:
    # Calculate the triangular number using the formula
    triangular_number = (counter * (counter + 1)) // 2  # Integer division

    # Calculate the difference
    difference = triangular_number - target_value

    # Check if we found a match
    if triangular_number == target_value:
        print(counter)  # We found a match
        break

    # Check if the triangular number is greater than the target value
    elif triangular_number > target_value:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(counter)  # A conditional match is met
            break

    # Increment the counter by 1
    counter += 1  # Move to the next counter value
