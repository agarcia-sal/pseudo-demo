# Function to determine if all elements in a boolean list can be marked
def mark_elements():
    # Read the size of the list
    n = int(input())
    
    # Initialize the boolean list with all positions unmarked (True)
    boolean_list = [True] * n
    
    # Set up iteration variables
    current_index = 0  # Tracks the current position in the list
    step = 1           # Step increment beginning from 1
    
    # Process to mark elements
    while step <= 500000:
        # Check current position
        if boolean_list[current_index] is True:
            # Mark this position as False (it has been marked)
            boolean_list[current_index] = False
        
        # Increment step value
        step += 1
        
        # Calculate the next position
        current_index = (current_index + step) % n
    
    # Extract remaining unmarked elements
    remaining_true = [val for val in boolean_list if val is True]
    
    # Check results
    if len(remaining_true) == 0:
        print("YES")  # All positions were marked
    else:
        print("NO")   # At least one position remains unmarked

# Call the function to execute
mark_elements()
