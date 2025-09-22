# Start the program

# Input the number
targetValue = abs(int(input()))

# Initialize a counter
counter = 0

# Begin an infinite loop
while True:
    # Calculate the triangular number
    triangularNumber = (counter * (counter + 1)) // 2

    # Calculate the difference
    difference = triangularNumber - targetValue

    # Check for a match
    if triangularNumber == targetValue:
        print(counter)  # Output the current value of counter
        break  # Terminate the loop

    # Check if triangular number exceeds targetValue
    if triangularNumber > targetValue:
        # Check if difference is an even number
        if difference % 2 == 0:
            print(counter)  # Output the current value of counter
            break  # Terminate the loop

    # Increment the counter
    counter += 1

# End the program
