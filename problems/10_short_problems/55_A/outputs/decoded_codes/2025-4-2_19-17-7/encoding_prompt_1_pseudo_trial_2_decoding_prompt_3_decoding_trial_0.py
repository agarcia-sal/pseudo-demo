def process():
    # Step 2: Input
    n = int(input())  # Read an integer value n from the user.
    
    # Step 3: Initialize
    isActive = [True] * n  # Create a list isActive of size n with all elements set to True.
    currentIndex = 0  # Set currentIndex to 0.
    increment = 1  # Set increment to 1.

    # Step 4: Loop, while incrementing increment up to 500,000
    for increment in range(1, 500001):
        if isActive[currentIndex]:  # If the value at isActive[currentIndex] is True
            isActive[currentIndex] = False  # Set isActive[currentIndex] to False
        
        # Update currentIndex to be the sum of currentIndex and increment, then take modulo n
        currentIndex = (currentIndex + increment) % n

    # Step 5: Check for Active Elements
    activeElements = [active for active in isActive if active]  # Create a list of active elements.

    # Step 6: Output
    if len(activeElements) == 0:  # If there are no active elements
        print('YES')
    else:  # Otherwise
        print('NO')

# Step 7: Call the process function to execute the program
process()
