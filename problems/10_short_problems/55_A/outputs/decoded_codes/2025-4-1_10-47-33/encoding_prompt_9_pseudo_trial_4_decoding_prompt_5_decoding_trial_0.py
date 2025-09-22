# Function to determine if all elements can be marked false based on the iterative process
def can_all_be_marked_false():
    # Read input: number of elements
    n = int(input())
    
    # Initialize the list to track marked positions
    marked = [True] * n
    
    # Initialize counters
    current_index = 0
    step_size = 1
    
    # Iterative marking process
    while step_size <= 500000:
        if marked[current_index]:  # Check if current index is still marked True
            marked[current_index] = False  # Mark it as False
        step_size += 1  # Increment the step size
        current_index = (current_index + step_size) % n  # Calculate next index
    
    # Check if any elements remain marked True
    remaining_true = [mark for mark in marked if mark]
    
    # Output result
    if len(remaining_true) == 0:
        print("YES")  # All elements can be marked false
    else:
        print("NO")   # Some elements remain marked true

# Sample usage
# can_all_be_marked_false()  # Uncomment to run the function
