def check_values_in_list():
    # Step 1: Read an integer value n from user input
    n = int(input())
    
    # Step 2: Create a list isActive of length n, initialized to True
    is_active = [True] * n
    
    # Step 3: Initialize currentIndex and increment
    current_index = 0
    increment = 1
    
    # Step 4: While increment is less than or equal to 500000
    while increment <= 500000:
        # Step 5: Check if the current index in is_active is True
        if is_active[current_index]:
            is_active[current_index] = False  # Set it to False
            
        # Step 6: Increment increment by 1
        increment += 1
        
        # Step 7: Update currentIndex
        current_index = (current_index + increment) % n  # Find the remainder when divided by n
    
    # Step 8: Create a list activeElements of the remaining True values
    active_elements = [active for active in is_active if active]
    
    # Step 9: Output based on the length of activeElements
    if len(active_elements) == 0:
        print("YES")
    else:
        print("NO")

# Execute the function
check_values_in_list()
