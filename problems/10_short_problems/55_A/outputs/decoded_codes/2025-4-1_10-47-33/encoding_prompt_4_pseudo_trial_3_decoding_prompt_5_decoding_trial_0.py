# Define a function to perform the pseudocode logic
def check_array():
    # Read a positive integer input for the size of the array
    n = int(input())

    # Initialize a boolean array of size n, all elements set to True
    boolean_array = [True] * n
    
    # Initialize variables
    index = 0  # This will track the index in the array
    increment = 1  # This will be incremented in the loop

    # Loop while increment is less than or equal to 500000
    while increment <= 500000:
        # If the current index in array boolean_array is True
        if boolean_array[index]:
            # Set the current index in array boolean_array to False
            boolean_array[index] = False
        
        # Increment i by 1
        increment += 1
        
        # Update index to the next index using the formula
        index = (index + increment) % n

    # Create a list of elements from boolean_array where elements are True
    true_elements = [value for value in boolean_array if value]
    
    # Check the length of the list true_elements
    if len(true_elements) == 0:
        # If true_elements is empty, output 'YES'
        print('YES')
    else:
        # If true_elements is not empty, output 'NO'
        print('NO')

# Call the function to execute the code
check_array()
