def checkAllFalseInList(n):
    # Initialize a list to track boolean values, all set to True initially
    booleanList = [True] * n
    
    # Set initial indices
    indexToModify = 0
    counter = 1
    
    # Loop until counter reaches 500000
    while counter <= 500000:
        # If the current boolean value is True, set it to False
        if booleanList[indexToModify] is True:
            booleanList[indexToModify] = False
        
        # Increment the counter for the next iteration
        counter += 1
        
        # Update indexToModify to the next position using the formula
        indexToModify = (indexToModify + counter) % n
    
    # Collect all the True values from the boolean list
    remainingTrueValues = [value for value in booleanList if value is True]
    
    # Check if there are any True values left
    if len(remainingTrueValues) == 0:
        print('YES')  # All values are set to False
    else:
        print('NO')   # There are still True values in the list

# Example usage
n = int(input())  # Read integer input for the size of the boolean list
checkAllFalseInList(n)
