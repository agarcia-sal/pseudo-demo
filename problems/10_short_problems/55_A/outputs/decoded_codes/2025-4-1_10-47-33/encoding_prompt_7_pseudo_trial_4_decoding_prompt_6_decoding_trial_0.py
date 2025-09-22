def check_condition(n):
    # Initialize a list 'is_active' of size n with all values set to True
    is_active = [True] * n
    index = 0
    increment = 1

    # Main loop: continue until increment is greater than 500,000
    while increment <= 500000:
        # Check if the current index is active
        if is_active[index]:
            # Mark the current index as inactive
            is_active[index] = False
        
        # Increment value for the next step
        increment += 1
        # Update index using modulo to wrap around the list
        index = (index + increment) % n

    # Create a list 'active_elements' containing the active (True) elements
    active_elements = [element for element in is_active if element]
    
    # Print 'YES' if no elements are active, else print 'NO'
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')

# Read an integer input
n = int(input())
# Call the function with the provided input
check_condition(n)
