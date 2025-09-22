def check_condition(n):
    # Initialize a list 'is_active' of size n with all values set to True
    is_active = [True] * n
    index = 0
    increment = 1
    
    # Loop until increment exceeds 500,000
    while increment <= 500000:
        # Check if the current index is active
        if is_active[index]:
            is_active[index] = False  # Mark as inactive
        
        increment += 1  # Increment the step
        index = (index + increment) % n  # Update index
        
    # Gather all active elements that are still True
    active_elements = [element for element in is_active if element]
    
    # Output based on the presence of active elements
    if len(active_elements) == 0:
        print('YES')  # No active elements left
    else:
        print('NO')   # Active elements still present

# Example usage:
n = int(input())
check_condition(n)
