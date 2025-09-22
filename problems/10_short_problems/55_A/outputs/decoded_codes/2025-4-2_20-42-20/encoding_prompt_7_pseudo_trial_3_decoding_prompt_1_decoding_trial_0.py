def checkConditionBasedOnInput(n):
    # Initialize a list of boolean values set to True for n elements
    booleanList = [True] * n
    
    # Initialize variables
    indexToToggle = 0
    incrementValue = 1
    
    # Loop through numbers from 1 to 500000
    while incrementValue <= 500000:
        # Check if the current position in booleanList is True
        if booleanList[indexToToggle]:
            # Set the current position in booleanList to False
            booleanList[indexToToggle] = False
        
        # Move to the next value to process
        incrementValue += 1
        
        # Update the index to toggle, wrapping it around the length of the list
        indexToToggle = (indexToToggle + incrementValue) % n
    
    # Create a new list of all true values from booleanList
    remainingTrueValues = [value for value in booleanList if value]
    
    # Check if there are any remaining true values
    if len(remainingTrueValues) == 0:
        # If none, print 'YES'
        print('YES')
    else:
        # If there's at least one true value, print 'NO'
        print('NO')

# Example usage (to be removed if only the function is needed):
n = int(input())
checkConditionBasedOnInput(n)
