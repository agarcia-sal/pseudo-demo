def checkCondition(n):
    # Initialize a list 'isActive' of size n with all values set to True
    isActive = [True] * n
    index = 0
    increment = 1
    
    # Loop while increment is less than or equal to 500,000
    while increment <= 500000:
        # If the current index is active, set it to inactive
        if isActive[index]:
            isActive[index] = False
        
        increment += 1
        index = (index + increment) % n  # Update index with wrap-around
    
    # Create a list of active elements remaining that are True
    activeElements = [elem for elem in isActive if elem]
    
    # Output 'YES' if there are no active elements left, else 'NO'
    if len(activeElements) == 0:
        print('YES')
    else:
        print('NO')
