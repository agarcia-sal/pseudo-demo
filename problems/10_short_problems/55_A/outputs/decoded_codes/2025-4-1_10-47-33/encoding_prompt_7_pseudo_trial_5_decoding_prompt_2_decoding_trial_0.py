def checkIfAllFalse(n):
    # INPUT: An integer n indicating the size of a boolean list
    # OUTPUT: Prints 'YES' if all values in the list are False, otherwise prints 'NO'

    # Initialize a list of boolean values all set to True
    booleanList = [True] * n  # Create a list of size n initialized to True
    index = 0
    step = 1

    # Iterate while step is less than or equal to 500000
    while step <= 500000:
        # If the current position in the booleanList is True
        if booleanList[index]:
            # Set the current position to False
            booleanList[index] = False
            
        # Increment step for the next iteration
        step += 1
        
        # Update index using circular indexing based on step
        index = (index + step) % n

    # Filter the booleanList to find all remaining True values
    remainingTrue = [value for value in booleanList if value]

    # If there are no True values remaining
    if len(remainingTrue) == 0:
        print('YES')
    else:
        print('NO')

# Example of calling the function
n = int(input())
checkIfAllFalse(n)
