# Start of the program

# Take an integer input from the user and store its absolute value
absoluteValue = abs(int(input()))

# Initialize a counter variable for the iterative process
counter = 0

# Start an infinite loop to calculate triangular numbers
while True:
    
    # Calculate the triangular number for the current counter position
    triangularNumber = (counter * (counter + 1)) // 2
    
    # Calculate the difference between the triangular number and the input value
    difference = triangularNumber - absoluteValue
    
    # Check if the triangular number is exactly equal to the input value
    if triangularNumber == absoluteValue:
        # Print the current counter as the result
        print(counter)
        # Exit the loop as the result is found
        break

    # Check if the triangular number exceeds the input value
    elif triangularNumber > absoluteValue:
        
        # Check if the difference is even
        if difference % 2 == 0:
            # Print the current counter as the result
            print(counter)
            # Exit the loop as the result is found
            break
    
    # Increment the counter to check the next triangular number
    counter += 1

# End of the program
