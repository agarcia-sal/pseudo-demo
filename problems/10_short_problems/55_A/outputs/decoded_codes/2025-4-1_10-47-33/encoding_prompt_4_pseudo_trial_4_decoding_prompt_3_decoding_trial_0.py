def check_boolean_list():
    # Read an integer from input
    n = int(input())

    # Initialize a list to track boolean values, with all values set to True
    boolean_list = [True] * n

    # Initialize indices
    current_index = 0
    counter = 1

    # Loop until counter exceeds 500000
    while counter <= 500000:
        # If the current index in the boolean list is True
        if boolean_list[current_index]:
            # Set the current index to False
            boolean_list[current_index] = False
        
        # Increment counter
        counter += 1
        
        # Update current index using modular arithmetic
        current_index = (current_index + counter) % n

    # Filter out the True values from the boolean list
    filtered_list = [val for val in boolean_list if val]

    # Check the length of the filtered list
    if len(filtered_list) == 0:
        print("YES")  # All positions were marked False
    else:
        print("NO")   # There are still True positions left

# Call the function to execute
check_boolean_list()
