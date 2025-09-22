# Start of the function
def mark_elements():
    # Read the total number of elements
    total_elements = int(input())
    
    # Initialize a list to track the status of each element, all set to True initially
    status_list = [True] * total_elements

    current_index = 0
    iteration_counter = 1

    # Loop until the iteration counter exceeds 500000
    while iteration_counter <= 500000:
        # If the current position in the status list is True, change it to False
        if status_list[current_index]:
            status_list[current_index] = False
            
        # Increment the iteration counter
        iteration_counter += 1
        
        # Update the index in the status list using the current iteration
        current_index = (current_index + iteration_counter) % total_elements

    # Create a list of all positions that are still True
    remaining_true_status = [status for status in status_list if status]

    # Check if there are no elements remaining that are True
    if len(remaining_true_status) == 0:
        print('YES')  # Indicating all elements have been marked
    else:
        print('NO')  # Indicating some elements are still marked True

# Call the function to execute
mark_elements()
