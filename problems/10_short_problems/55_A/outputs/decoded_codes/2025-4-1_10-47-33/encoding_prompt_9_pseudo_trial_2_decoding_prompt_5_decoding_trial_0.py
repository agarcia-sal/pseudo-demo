# Function to determine if all elements in a boolean list can be set to false
def can_all_be_false():
    # Receive input for the size of the list
    list_size = int(input())
    
    # Initialize boolean list with all True values
    boolean_list = [True] * list_size
    
    # Initialize iteration variables
    current_index = 0
    step = 1
    
    # Loop through iterations with a maximum of 500,000 steps
    while step <= 500000:
        # Check if the current position is True
        if boolean_list[current_index]:
            # Set the current position to False
            boolean_list[current_index] = False
        # Increment the step
        step += 1
        # Update the current index with wrapping around using modulo
        current_index = (current_index + step) % list_size
    
    # Create a list of remaining True values
    remaining_true = [value for value in boolean_list if value]
    
    # Output the result based on the remaining True values
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Uncomment the line below to run the function when needed
# can_all_be_false()
