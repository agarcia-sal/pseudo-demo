def process_elements():
    # Step 1: Input the number of elements
    number_of_elements = int(input())

    # Step 2: Create a list to track boolean values, initialized to True
    boolean_list = [True] * number_of_elements

    # Initialize variables for iteration
    index = 0
    iterator = 1

    # Step 3: Loop through a range of values
    while iterator <= 500000:
        # Step 4: If current boolean value is True
        if boolean_list[index]:
            # Mark it as False
            boolean_list[index] = False
        
        # Increment iterator
        iterator += 1

        # Calculate the next index to modify using the modulo operation
        index = (index + iterator) % number_of_elements
    
    # Step 5: Create a new list of remaining True values
    remaining_true_values = [value for value in boolean_list if value]

    # Step 6: Check if there are any True values left
    if len(remaining_true_values) == 0:
        print('YES')
    else:
        print('NO')

# Call the function
process_elements()
