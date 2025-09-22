def check_condition(n):
    # Initialize a list 'is_active' of size n with all values set to True
    is_active = [True] * n
    index = 0
    increment = 1

    # Main loop runs while increment is less than or equal to 500,000
    while increment <= 500000:
        # If current index position is True, set it to False
        if is_active[index]:
            is_active[index] = False
        
        # Increment the number and calculate the new index
        increment += 1
        index = (index + increment) % n

    # Compile a list of active elements that are still True
    active_elements = [active for active in is_active if active]
    
    # Print results based on the length of active elements
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')

# Example usage:
n = int(input())
check_condition(n)
