def check_condition(n):
    # Initialize a list 'isActive' with all values set to True
    is_active = [True] * n
    index = 0
    increment = 1
    
    # Loop until 'increment' exceeds 500,000
    while increment <= 500000:
        # If the current index is active, set it to inactive
        if is_active[index]:
            is_active[index] = False
        
        # Increment the value of 'increment'
        increment += 1
        # Update 'index' with modular arithmetic
        index = (index + increment) % n
    
    # Create a list of active elements remaining
    active_elements = [ele for ele in is_active if ele]
    
    # Print 'YES' if no active elements remain, otherwise print 'NO'
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')

# Example usage:
# n = int(input())
# check_condition(n)
