def check_array_status(size):
    # Initialize an array 'is_active' of boolean values, all set to True
    is_active = [True] * size
    index = 0
    iteration = 1

    # Loop for a maximum of 500000 iterations
    while iteration <= 500000:
        if is_active[index]:
            # Set the current index in is_active to False
            is_active[index] = False

        # Update iteration count and index
        iteration += 1
        index = (index + iteration) % size

    # Initialize an array 'active_elements' to store still active elements
    active_elements = [element for element in is_active if element]

    # Check if active_elements is empty and print the result
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')

# To test the function, you would typically call it with an integer input.
# Example call (uncomment the next line to test within a script):
# check_array_status(int(input()))
