def process_boolean_list():
    # Read an integer input for the size of the list
    number_of_elements = int(input())
    
    # Create a boolean list initialized to True for each index
    boolean_list = [True] * number_of_elements
    
    # Initialize variables for processing
    index = 0
    increment = 1

    # Loop while increment is less than or equal to 500,000
    while increment <= 500000:
        # If the current boolean value at index is True, set it to False
        if boolean_list[index]:
            boolean_list[index] = False
        
        # Increment the counter
        increment += 1
        
        # Calculate the next index using modular arithmetic
        index = (index + increment) % number_of_elements
    
    # Create a new list that contains only the True values from boolean_list
    remaining_true_values = [value for value in boolean_list if value]
    
    # Check if there are no remaining True values and output result accordingly
    if len(remaining_true_values) == 0:
        print('YES')
    else:
        print('NO')

# Test the function
if __name__ == "__main__":
    process_boolean_list()
