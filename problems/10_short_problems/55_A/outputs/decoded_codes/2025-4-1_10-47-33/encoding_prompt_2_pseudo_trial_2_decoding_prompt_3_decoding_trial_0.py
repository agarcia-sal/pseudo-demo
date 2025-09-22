def check_values_in_list():
    # Step 2: Read an integer value n from user input
    n = int(input())
    
    # Step 3: Create a list isActive of length n, initially set to True
    isActive = [True] * n
    
    # Step 4: Initialize currentIndex and increment variables
    currentIndex = 0
    increment = 1
    
    # Step 6: Loop while increment is less than or equal to 500000
    while increment <= 500000:
        # Step 6.1: Check if the current index in isActive is True
        if isActive[currentIndex]:
            # Step 6.1.1: Set the element at currentIndex to False
            isActive[currentIndex] = False

        # Step 6.2: Increment increment by 1
        increment += 1
        
        # Step 6.3: Update currentIndex
        currentIndex = (currentIndex + increment) % n

    # Step 7: Create a list activeElements with remaining True values
    activeElements = [value for value in isActive if value]

    # Step 8: Check if the length of activeElements is equal to 0
    if len(activeElements) == 0:
        # Output "YES" if no True values are left
        print("YES")
    else:
        # Output "NO" if there are still True values
        print("NO")

# Run the function
check_values_in_list()
