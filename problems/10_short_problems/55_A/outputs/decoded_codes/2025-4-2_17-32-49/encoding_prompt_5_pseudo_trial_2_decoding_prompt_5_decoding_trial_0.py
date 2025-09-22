# Function to determine if any "TRUE" values remain in the list after processing
def check_remaining_true_values():
    # Read the size of the list from user input
    n = int(input())
    
    # Initialize a list of size n with all values set to TRUE
    b = [True] * n
    
    # Initialize index variables
    j = 0  # Current position in the list
    i = 1  # Iteration counter
    
    # Process the list
    while i <= 500000:
        # Check if the current position is still TRUE
        if b[j]:  # If b[j] is TRUE
            b[j] = False  # Mark this position as visited by setting it to FALSE
        
        # Increment i for the next iteration
        i += 1
        
        # Update index j to the next position using modulo operation
        j = (j + i) % n  # Wrap around if needed
    
    # Create a new list with remaining TRUE values
    remaining_true_values = [value for value in b if value]

    # Determine if any TRUE values remain
    if len(remaining_true_values) == 0:
        print("YES")  # All positions were marked as visited
    else:
        print("NO")   # Some positions remain unvisited

# Uncomment to run the function
# check_remaining_true_values()
