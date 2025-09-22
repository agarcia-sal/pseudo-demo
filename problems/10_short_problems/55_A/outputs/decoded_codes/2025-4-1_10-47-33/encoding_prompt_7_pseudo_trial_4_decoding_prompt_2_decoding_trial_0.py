def checkCondition(n):
    # Initialize the isActive list with all values set to True
    isActive = [True] * n
    index = 0
    increment = 1
    
    # Main loop until increment exceeds 500,000
    while increment <= 500000:
        # If the current index is active, set it to False
        if isActive[index]:
            isActive[index] = False
        
        # Increment the increment value
        increment += 1
        
        # Update the index using modular arithmetic
        index = (index + increment) % n
    
    # Create a list of active elements
    activeElements = [elem for elem in isActive if elem]
    
    # Print 'YES' if there are no active elements left, else print 'NO'
    if len(activeElements) == 0:
        print('YES')
    else:
        print('NO')

# Example usage:
n = int(input())
checkCondition(n)
