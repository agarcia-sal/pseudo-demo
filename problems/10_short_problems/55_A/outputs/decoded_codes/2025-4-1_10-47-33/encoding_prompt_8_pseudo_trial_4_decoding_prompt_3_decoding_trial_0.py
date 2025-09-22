def check_remaining_true_values():
    # Step 1: Read input from the user
    total_numbers = int(input())
    
    # Step 2: Initialize a list with all entries set to True
    status_list = [True] * total_numbers
    
    # Step 3: Set initial indices
    current_index = 0
    step = 1
    
    # Step 4: Loop until the step limit is reached
    while step <= 500000:
        if status_list[current_index]:  # Check if the current index is True
            status_list[current_index] = False  # Mark it as False
        
        step += 1  # Increase the step
        current_index = (current_index + step) % total_numbers  # Update current index in a circular manner
    
    # Step 5: Filter the remaining True values
    remaining_true_values = [value for value in status_list if value]
    
    # Step 6: Output the result based on the remaining True values
    if len(remaining_true_values) == 0:
        print("YES")  # No True values left
    else:
        print("NO")   # At least one True value remains

# Call the function to execute the program
check_remaining_true_values()
