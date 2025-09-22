def main():
    # Read an integer input representing the size of the array
    size_of_array = int(input())
    
    # Initialize a boolean array where all elements are set to True
    boolean_array = [True] * size_of_array

    # Set initial values for index variables
    index_for_increment = 0
    counter = 1

    # Iterate a maximum of 500,000 times
    while counter <= 500000:
        # If the current position in the boolean array is true
        if boolean_array[index_for_increment]:
            # Mark the current position as false
            boolean_array[index_for_increment] = False

        # Update the counter for the next iteration
        counter += 1
        
        # Calculate the next index using modulo operation
        index_for_increment = (index_for_increment + counter) % size_of_array

    # Create a new list containing only True values from the boolean array
    true_values_list = [val for val in boolean_array if val]

    # Check if the list of true values is empty
    if len(true_values_list) == 0:
        # Print 'YES' if there are no True values remaining
        print('YES')
    else:
        # Print 'NO' if there are still True values
        print('NO')

if __name__ == "__main__":
    main()
