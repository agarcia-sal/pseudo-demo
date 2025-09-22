# Start the program

# Get user input
targetValue = abs(int(input()))  # Read the input and take the absolute value

# Initialize a counter
counter = 0

# Begin an endless loop to find the triangular number
while True:
    # Calculate the triangular number
    triangularNumber = (counter * (counter + 1)) // 2
    
    # Calculate the difference
    difference = triangularNumber - targetValue
    
    # Check if triangularNumber equals targetValue
    if triangularNumber == targetValue:
        print(counter)  # Match found
        break  # Exit the loop
    
    # Check if triangularNumber is greater than targetValue
    elif triangularNumber > targetValue:
        # Check if the difference is even
        if difference % 2 == 0:
            print(counter)  # Condition met
            break  # Exit the loop

    # Increment the counter
    counter += 1  # Move to the next counter value

# End the program
