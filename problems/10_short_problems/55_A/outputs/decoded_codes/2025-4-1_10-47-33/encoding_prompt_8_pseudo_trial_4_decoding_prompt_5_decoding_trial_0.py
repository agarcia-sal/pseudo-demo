# Function to determine if any True values remain in the list after operations
def check_status_values():
    # Read input for the number of entries
    total_numbers = int(input())
    
    # Initialize a list with all entries set to True
    status_list = [True] * total_numbers
    
    # Set initial indices for loop control
    current_index = 0
    step = 1
    
    # Loop until step exceeds 500,000
    while step <= 500000:
        # Mark the current index as False if it's True
        if status_list[current_index]:
            status_list[current_index] = False
        
        # Increment the step
        step += 1
        
        # Update current_index in a circular fashion
        current_index = (current_index + step) % total_numbers
    
    # Check for remaining True values
    remaining_true_values = [value for value in status_list if value]
    
    # Output result based on the length of remaining True values
    if len(remaining_true_values) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the logic
check_status_values()
