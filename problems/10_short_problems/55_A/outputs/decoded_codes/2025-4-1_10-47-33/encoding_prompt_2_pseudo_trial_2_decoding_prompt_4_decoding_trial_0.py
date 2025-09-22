def check_values_in_list():
    # Step 2: Read an integer value n from user input
    n = int(input())
    
    # Step 3: Create a list isActive of length n with all elements set to True
    is_active = [True] * n
    
    # Step 4: Initialize currentIndex and increment
    current_index = 0
    increment = 1
    
    # Step 6: While increment is less than or equal to 500000
    while increment <= 500000:
        # Step 6.1: If the element at currentIndex is True
        if is_active[current_index]:
            # Step 6.1.1: Set the element at currentIndex to False
            is_active[current_index] = False
        
        # Step 6.2: Increment increment by 1
        increment += 1
        
        # Step 6.3: Update currentIndex using modulo to wrap around
        current_index = (current_index + increment) % n
    
    # Step 7: Create a list of active elements (still True)
    active_elements = [element for element in is_active if element]
    
    # Step 8: Check the length of activeElements
    if len(active_elements) == 0:
        # Step 8.1: Output "YES"
        print("YES")
    else:
        # Step 9.1: Output "NO"
        print("NO")

# Step 1: Begin the program
check_values_in_list()
