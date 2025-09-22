# Start the program

# Get user input
targetValue = abs(int(input()))
 
# Initialize a counter
counter = 0

# Begin an endless loop to find the triangular number
while True:
    # Calculate the triangular number
    triangularNumber = (counter * (counter + 1)) // 2
    
    # Calculate the difference
    difference = triangularNumber - targetValue
    
    # Check if triangular number equals target value
    if triangularNumber == targetValue:
        print(counter)  # Found a match
        break
    
    # Check if triangular number is greater than target value
    elif triangularNumber > targetValue:
        # Check if difference is an even number
        if difference % 2 == 0:
            print(counter)  # Different condition met
            break
    
    # Increment the counter
    counter += 1

# End the program
