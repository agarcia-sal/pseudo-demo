def checkCondition(n):
    # Initialize a list of boolean values, all set to True
    booleanList = [True] * n
    index = 0
    increment = 1

    # Loop through a range until increment reaches 500000
    while increment <= 500000:
        # If the current position in the booleanList is True
        if booleanList[index]:
            # Set the current position to False
            booleanList[index] = False
        
        # Move to the next increment
        increment += 1
        # Update the index based on the increment value and total size n
        index = (index + increment) % n

    # Create a list of all remaining True values in booleanList
    remainingTrueValues = [value for value in booleanList if value]

    # Check if there are no True values remaining
    if len(remainingTrueValues) == 0:
        print('YES')
    else:
        print('NO')

# Example use case: 
# Uncomment and run the following line for testing
# checkCondition(int(input()))
