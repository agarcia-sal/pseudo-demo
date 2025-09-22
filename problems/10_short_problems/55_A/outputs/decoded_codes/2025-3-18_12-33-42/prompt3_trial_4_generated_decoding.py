def process_boolean_array():
    # Step 1: Read an integer input representing the size of the array
    size_of_array = int(input())

    # Step 2: Initialize a boolean array to track status (all elements start as True)
    boolean_array = [True] * size_of_array

    # Step 3: Initialize variables for control
    index_increment = 1
    current_index = 0

    # Step 4: Loop until index_increment exceeds 500000
    while index_increment <= 500000:
        
        # Step 5: If current index in boolean_array is True
        if boolean_array[current_index]:
            # Step 6: Mark current index as False
            boolean_array[current_index] = False
        
        # Step 7: Prepare for the next iteration
        index_increment += 1
        
        # Step 8: Update the current_index based on current_index and index_increment
        current_index = (current_index + index_increment) % size_of_array

    # Step 9: Filter the boolean_array to find all True values
    true_values_list = [element for element in boolean_array if element]

    # Step 10: Check if there are any remaining True values
    if len(true_values_list) == 0:
        print('YES')  # Indicating there are no True values left
    else:
        print('NO')   # Indicating there are still True values remaining

# Call the function to run the process
process_boolean_array()
