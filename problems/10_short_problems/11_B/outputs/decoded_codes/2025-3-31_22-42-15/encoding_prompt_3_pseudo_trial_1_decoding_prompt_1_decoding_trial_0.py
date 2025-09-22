# BEGIN

# Get the absolute value of the integer input from the user
absoluteValue = abs(int(input()))

# Initialize a counter for triangular numbers
index = 0

# Infinite loop to calculate triangular numbers
while True:
    
    # Calculate the triangular number for the current index
    triangularNumber = (index * (index + 1)) // 2
    
    # Calculate the difference between the triangular number and the user input
    difference = triangularNumber - absoluteValue
    
    # Check if the triangular number equals the user input
    if triangularNumber == absoluteValue:
        # If they are equal, print the current index
        print(index)
        # Exit the loop
        break
    
    # Check if the triangular number exceeds the user input
    elif triangularNumber > absoluteValue:
        # If the difference is even
        if difference % 2 == 0:
            # Print the current index
            print(index)
            # Exit the loop
            break

    # Increment the index to check the next triangular number
    index += 1

# END
