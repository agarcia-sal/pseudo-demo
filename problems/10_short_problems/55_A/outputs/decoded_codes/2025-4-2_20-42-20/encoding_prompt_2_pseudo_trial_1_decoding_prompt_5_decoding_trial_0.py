# Start the program
def check_availability():
    # Get an integer input from the user
    number_of_elements = int(input())
    
    # Create a list initialized to True with the specified number of elements
    is_available = [True] * number_of_elements
    
    # Initialize index and increment
    index = 0
    increment = 1
    
    # Loop while increment is less than or equal to 500000
    while increment <= 500000:
        # Check if the current index is available
        if is_available[index]:
            # Set the current element to False
            is_available[index] = False
        
        # Increase increment by 1
        increment += 1
        
        # Update index using modulo operation
        index = (index + increment) % number_of_elements
    
    # Create a list of remaining True elements
    remaining_true = [element for element in is_available if element]
    
    # Check if any elements are still available
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Call the function to execute
check_availability()
