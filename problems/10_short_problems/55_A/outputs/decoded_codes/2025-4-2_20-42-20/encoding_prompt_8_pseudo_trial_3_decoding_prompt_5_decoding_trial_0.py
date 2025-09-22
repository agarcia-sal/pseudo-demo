# Function to determine if all boolean values in a list are False after a series of updates
def boolean_update_process():
    # Step 1: Get the number of boolean elements from the user
    n = int(input())  # Read the total number of boolean elements

    # Step 2: Create a list of boolean values, all initially set to True
    boolean_list = [True] * n

    # Step 3: Initialize current index and increment value
    current_index = 0
    increment = 1

    # Step 4: Define a limit for the number of updates
    limit = 500000

    # Update loop
    while increment <= limit:
        # If the current index in boolean list is True
        if boolean_list[current_index]:
            # Set the current index in boolean list to False
            boolean_list[current_index] = False
        
        # Increase the increment value for the next step
        increment += 1
        
        # Update current index using modulo to stay within list bounds
        current_index = (current_index + increment) % n

    # Step 5: Check for remaining True values
    remaining_true = [value for value in boolean_list if value]

    # Step 6: Output the result based on the presence of remaining True values
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Call the function to execute the process
boolean_update_process()
