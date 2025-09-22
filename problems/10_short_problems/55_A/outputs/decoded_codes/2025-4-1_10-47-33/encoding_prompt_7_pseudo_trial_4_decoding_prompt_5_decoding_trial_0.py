def check_condition(n):
    # Initialize a list 'is_active' of size n with all values set to True
    is_active = [True] * n
    index = 0
    increment = 1
    
    # Loop until increment is greater than 500,000
    while increment <= 500000:
        # If the current index in is_active is True
        if is_active[index]:
            # Set that index to False, marking it inactive
            is_active[index] = False
        
        # Increment the value of increment
        increment += 1
        # Update index using modular arithmetic to wrap around
        index = (index + increment) % n
    
    # Create a list of elements that are still True in is_active
    active_elements = [elem for elem in is_active if elem]
    
    # Check if there are no active elements left
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')

# Example to test the function
# check_condition(10)  # You can uncomment this line to test the function with input
