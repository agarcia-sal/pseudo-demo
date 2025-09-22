# Start the program

# Get user input
targetValue = abs(int(input()))  # Store the absolute value of user-entered number

# Initialize a counter
counter = 0

# Begin an endless loop to find the triangular number
while True:
    # Calculate the triangular number using the formula
    triangularNumber = (counter * (counter + 1)) // 2  # Use integer division for whole number result
    
    # Calculate the difference
    difference = triangularNumber - targetValue
    
    # Check if the triangular number equals target value
    if triangularNumber == targetValue:
        print(counter)  # Print the counter if a match is found
        break  # Exit the loop
    
    # Check if the triangular number is greater than target value
    elif triangularNumber > targetValue:
        # Check if the difference is even
        if difference % 2 == 0:
            print(counter)  # Print the counter for this condition
            break  # Exit the loop
    
    # Increment the counter to check the next triangular number
    counter += 1

# End of program
