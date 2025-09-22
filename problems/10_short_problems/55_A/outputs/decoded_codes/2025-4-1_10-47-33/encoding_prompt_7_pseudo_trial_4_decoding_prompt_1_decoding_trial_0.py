def checkCondition(n):
    # Initialize a list 'isActive' of size n with all values set to True
    isActive = [True] * n
    
    # Set index to 0 and increment to 1
    index = 0
    increment = 1
    
    # While increment is less than or equal to 500000
    while increment <= 500000:
        # If isActive[index] is True
        if isActive[index]:
            # Set isActive[index] to False
            isActive[index] = False
        
        # Increment increment by 1
        increment += 1
        
        # Update index to (index + increment) MOD n
        index = (index + increment) % n
    
    # Initialize a list 'activeElements' with all elements from isActive that are True
    activeElements = [value for value in isActive if value]
    
    # If the length of activeElements is zero
    if len(activeElements) == 0:
        # Print 'YES'
        print('YES')
    else:
        # Print 'NO'
        print('NO')
