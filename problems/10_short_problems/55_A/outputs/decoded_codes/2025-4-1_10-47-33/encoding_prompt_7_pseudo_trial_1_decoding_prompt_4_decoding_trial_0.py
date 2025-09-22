def check_array_status(size):
    # Initialize an array 'is_active' with 'size' elements, all set to True
    is_active = [True] * size
    index = 0
    iteration = 1

    # Loop until the iteration count reaches 500,000
    while iteration <= 500000:
        # If the current index is active, mark it as inactive
        if is_active[index]:
            is_active[index] = False
        
        # Prepare for the next iteration
        iteration += 1
        index = (index + iteration) % size

    # Collect all elements that remain True in 'active_elements'
    active_elements = [element for element in is_active if element]

    # Print 'YES' if there are no active elements, otherwise print 'NO'
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')


# Example of how to call the function (for testing purposes):
# size = int(input())
# check_array_status(size)
