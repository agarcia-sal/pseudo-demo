# Function to execute the logic based on the pseudocode description
def check_remaining_true_values():
    # Read the size of the list from the user
    list_size = int(input())
    
    # Create a boolean list initialized to True for all indices up to list_size
    boolean_list = [True] * list_size
    
    # Initialize indices for iteration
    current_index = 0
    increment = 1

    # Loop until increment reaches 500,000
    while increment <= 500000:
        # Check if the current index in the boolean list is True
        if boolean_list[current_index]:
            # Set the current index in the boolean list to False
            boolean_list[current_index] = False
        
        # Increment the counter for the next iteration
        increment += 1
        
        # Calculate the next index using modulus to wrap around the list
        current_index = (current_index + increment) % list_size
    
    # Create a new list containing all the True values from the boolean list
    remaining_true_values = [value for value in boolean_list if value]
    
    # Check if there are any remaining True values
    if len(remaining_true_values) == 0:
        # No True values remain, print 'YES'
        print('YES')
    else:
        # There are still True values, print 'NO'
        print('NO')

# Call the function to execute
check_remaining_true_values()
