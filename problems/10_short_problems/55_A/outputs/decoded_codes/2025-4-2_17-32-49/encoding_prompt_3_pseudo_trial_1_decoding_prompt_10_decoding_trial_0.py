def main():
    # Read an integer input representing the size of the list
    list_size = int(input())
    
    # Create a boolean list initialized to True
    boolean_list = [True] * list_size
    
    index = 0  # Start index for the boolean list
    current_number = 1  # Starting point for the iterative process

    # Loop until current_number reaches 500000
    while current_number <= 500000:
        # If the current index in the boolean list is True
        if boolean_list[index]:
            # Mark this index as False
            boolean_list[index] = False
        
        # Move to the next number
        current_number += 1

        # Update the index using the formula (index + current_number) modulo list_size
        index = (index + current_number) % list_size

    # Create a new list to collect all True values from the boolean list
    true_values_list = [value for value in boolean_list if value]

    # Check if the list of True values is empty
    if len(true_values_list) == 0:
        print('YES')  # Output YES if no True values are found
    else:
        print('NO')   # Output NO if there are still True values found

if __name__ == "__main__":
    main()
