def main():
    # Read a positive integer input for the size of the array
    n = int(input())

    # Initialize a boolean array of size n, all elements set to True
    boolean_array = [True] * n
    
    # Initialize variables
    current_index = 0  # This will track the index in the array
    i = 1  # This will be incremented in the loop

    # Loop while i is less than or equal to 500000
    while i <= 500000:
        # If the current index in array boolean_array is True
        if boolean_array[current_index]:
            # Set the current index in array boolean_array to False
            boolean_array[current_index] = False
        
        # Increment i by 1
        i += 1
        
        # Update current_index to the next index using the formula
        current_index = (current_index + i) % n

    # Create a list with all True values from boolean_array
    true_values = [val for val in boolean_array if val]

    # Check the length of the list true_values
    if len(true_values) == 0:
        # If true_values is empty, output 'YES'
        print('YES')
    else:
        # If true_values is not empty, output 'NO'
        print('NO')

# To run the main function when the script is executed
if __name__ == "__main__":
    main()
