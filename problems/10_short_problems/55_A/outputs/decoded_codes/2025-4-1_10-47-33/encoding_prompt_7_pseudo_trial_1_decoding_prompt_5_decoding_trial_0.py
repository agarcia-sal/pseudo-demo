def check_array_status(size):
    # Initialize an array of boolean values with size elements, all set to True
    is_active = [True] * size
    index = 0
    iteration = 1

    # Loop for a maximum of 500000 iterations
    while iteration <= 500000:
        # If current index is active, mark it as inactive
        if is_active[index]:
            is_active[index] = False

        # Move to the next iteration
        iteration += 1
        index = (index + iteration) % size  # Update index with wrapping

    # Initialize an array to store all active elements
    active_elements = []

    # Collect all elements that are still True
    for element in is_active:
        if element:
            active_elements.append(element)

    # Check if we have any active elements left and print the result
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')


# Example of how to use the function (not part of the function itself)
# size_input = int(input())
# check_array_status(size_input)
