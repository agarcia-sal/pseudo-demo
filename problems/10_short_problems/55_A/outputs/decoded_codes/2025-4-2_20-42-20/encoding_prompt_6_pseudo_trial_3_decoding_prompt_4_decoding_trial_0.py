def main():
    # Read an integer input which represents the size of a list.
    list_size = int(input())

    # Create a boolean list initialized to True for all indices up to list_size.
    boolean_list = [True] * list_size

    # Initialize variables for iteration.
    current_index = 0
    increment = 1

    # Loop until increment reaches 500,000.
    while increment <= 500000:
        # Check if the current index in the boolean list is True.
        if boolean_list[current_index]:
            # Set the current index in the boolean list to False.
            boolean_list[current_index] = False
        
        # Increment the counter for the next iteration.
        increment += 1
        
        # Calculate the next index by adding the increment and wrapping around the list using modulus.
        current_index = (current_index + increment) % list_size

    # Create a new list containing all the True values from the boolean list.
    remaining_true_values = [value for value in boolean_list if value]

    # Check if there are any remaining True values.
    if not remaining_true_values:
        # If no True values remain, print 'YES'.
        print('YES')
    else:
        # If there are still True values, print 'NO'.
        print('NO')

# Calling the main function
if __name__ == "__main__":
    main()
