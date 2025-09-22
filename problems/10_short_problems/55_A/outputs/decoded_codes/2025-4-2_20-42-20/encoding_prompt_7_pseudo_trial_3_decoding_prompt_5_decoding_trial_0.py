def check_condition_based_on_input(n):
    # Initialize a list of boolean values set to True for n elements
    boolean_list = [True] * n
    
    # Initialize variables
    index_to_toggle = 0
    increment_value = 1
    
    # Loop through numbers from 1 to 500000
    while increment_value <= 500000:
        # Check if the current position in boolean_list is True
        if boolean_list[index_to_toggle]:
            # Set the current position in boolean_list to False
            boolean_list[index_to_toggle] = False
        
        # Move to the next value to process
        increment_value += 1
        # Update the index to toggle, wrapping it around the length of the list
        index_to_toggle = (index_to_toggle + increment_value) % n
    
    # Create a new list of all true values from boolean_list
    remaining_true_values = [value for value in boolean_list if value]
    
    # Check if there are any remaining true values
    if len(remaining_true_values) == 0:
        # If none, print 'YES'
        print('YES')
    else:
        # If there's at least one true value, print 'NO'
        print('NO')

# Example test case for demonstration
# check_condition_based_on_input(10)  # Uncomment to test with n = 10
