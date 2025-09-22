def check_array_status(size):
    # Initialize an array 'isActive' with 'size' elements, all set to True
    is_active = [True] * size
    
    index = 0
    iteration = 1

    # Loop until the maximum iterations of 500000
    while iteration <= 500000:
        # Mark the current index as inactive if it is still active
        if is_active[index]:
            is_active[index] = False
        
        # Update the index for the next iteration
        iteration += 1
        index = (index + iteration) % size

    # Collecting all active elements
    active_elements = [element for element in is_active if element]

    # Print result based on the presence of active elements
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')

# Example usage of the function
# Uncomment the following lines to test the function
# size = int(input())
# check_array_status(size)
