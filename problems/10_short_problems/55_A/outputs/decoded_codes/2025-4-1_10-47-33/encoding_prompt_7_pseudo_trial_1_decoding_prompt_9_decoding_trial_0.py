def check_array_status(size):
    # Initialize an array 'isActive' of boolean values with 'size' elements, all set to True
    is_active = [True] * size
    index = 0
    iteration = 1

    # Loop through iterations up to 500000
    while iteration <= 500000:
        if is_active[index]:  # Check if the current index is active
            is_active[index] = False  # Mark the current index as inactive

        iteration += 1  # Increase iteration by 1
        index = (index + iteration) % size  # Update index in a circular manner

    # Initialize an array 'active_elements' to store elements of isActive that are still True
    active_elements = [element for element in is_active if element]

    # Final check for the status of active elements
    if len(active_elements) == 0:
        print('YES')  # If no active elements, print 'YES'
    else:
        print('NO')  # If there are active elements, print 'NO'

# Example usage (you can uncomment the following lines to run):
# size_input = int(input())
# check_array_status(size_input)
