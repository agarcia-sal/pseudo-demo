# Function to determine if all elements in a list can be marked as false
def can_mark_all_false():
    # Read the number of elements
    n = int(input())
    
    # Initialize the marked list with all elements set to True
    marked = [True] * n
    
    # Initialize counters
    current_index = 0  # Position being processed
    step_size = 1      # Increment for marking

    # Iterative marking process
    while step_size <= 500000:
        # If the current position is marked as True
        if marked[current_index]:
            # Mark it as False
            marked[current_index] = False
        
        # Increment the step size for the next position calculation
        step_size += 1
        
        # Calculate the next position using modulo
        current_index = (current_index + step_size) % n
    
    # Check how many remain True
    remaining_true = [x for x in marked if x]  # List comprehension to filter True values

    # Output result based on remaining marked elements
    if len(remaining_true) == 0:
        print("YES")  # All elements were marked as False
    else:
        print("NO")   # There are still True elements left

# Sample invocation of the function
can_mark_all_false()
