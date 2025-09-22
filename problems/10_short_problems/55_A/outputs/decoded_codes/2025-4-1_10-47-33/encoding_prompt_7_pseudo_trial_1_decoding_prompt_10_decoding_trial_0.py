def check_array_status(size):
    # Initialize an array of boolean values with 'size' elements, all set to True
    is_active = [True] * size
    index = 0
    iteration = 1

    # Loop to mark elements as inactive based on the given logic
    while iteration <= 500000:
        if is_active[index]:
            is_active[index] = False
        
        iteration += 1
        index = (index + iteration) % size

    # Create a list to store active elements
    active_elements = [element for element in is_active if element]

    # Check if there are any active elements remaining
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')


# Test cases
def test_check_array_status():
    # Boundary case
    check_array_status(1)  # Expected output: NO (1 element becomes inactive)
    check_array_status(2)  # Expected output: NO (both elements become inactive)
    check_array_status(3)  # Output could vary based on the marking logic
    check_array_status(10) # A larger case

# Uncomment to run tests
# test_check_array_status()
