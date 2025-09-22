# Function to determine if all elements in a list can be marked 'False'
def mark_elements():
    # Read number of elements
    n = int(input())
    
    # Initialize list with 'True' values
    b = [True] * n
    
    # Initialize indices for tracking
    j = 0  # current index in list
    i = 1  # step counter
    
    # Iterate to mark values in the list
    while i <= 500000:
        # Check if the current index in list 'b' is 'True'
        if b[j]:
            # Mark the current index as 'False'
            b[j] = False
        
        # Increment the step counter
        i += 1
        
        # Update the index 'j'
        j = (j + i) % n  # wrap around using modulo
    
    # Create a new list containing only 'True' values
    x = [value for value in b if value]

    # Check if there are any 'True' values remaining and output result
    if len(x) == 0:
        print("YES")
    else:
        print("NO")

# Call the function
mark_elements()
