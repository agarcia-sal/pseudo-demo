def check_status_of_elements(size_of_array):
    # Initialize array 'b' of size n with all values set to True
    b = [True] * size_of_array
    index_j = 0  # Initialize index j
    counter_i = 1  # Initialize counter i

    # Looping to modify the array based on the specified logic
    while counter_i <= 500000:
        if b[index_j]:  # If the element at index j is True
            b[index_j] = False  # Set it to False
        counter_i += 1  # Increment counter i
        index_j = (index_j + counter_i) % size_of_array  # Update index j

    # Create a new array 'x' containing all True values remaining in array 'b'
    x = [value for value in b if value]

    # Check the length of array 'x' to determine output
    if len(x) == 0:
        print('YES')  # All elements in 'b' have been set to False
    else:
        print('NO')  # There are still True elements in 'b'

# Example usage: Uncomment the line below to test the function
# check_status_of_elements(int(input()))
