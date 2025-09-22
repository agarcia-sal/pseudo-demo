# Start the program

# Get user input
targetValue = abs(int(input()))

# Initialize a counter
counter = 0

# Begin an endless loop to find the triangular number
while True:
    # Calculate the triangular number
    triangularNumber = (counter * (counter + 1)) / 2
    
    # Calculate the difference
    difference = triangularNumber - targetValue
    
    # Check for conditions
    if triangularNumber == targetValue:
        # Print the counter if a match is found
        print(counter)
        break  # Exit the loop

    elif triangularNumber > targetValue:
        # If the triangular number is greater, check if the difference is even
        if difference % 2 == 0:
            # Print the counter for the different condition
            print(counter)
            break  # Exit the loop

    # Increment the counter for the next iteration
    counter += 1

# End the program
