def process_elements():
    # Read the total number of elements
    total_elements = int(input())
    
    # Initialize the isActive list and control variables
    is_active = [True] * total_elements  # All elements are initially active
    index = 0
    step = 1

    # Loop until the step variable exceeds 500,000
    while step <= 500000:
        # Check if the current index is still active
        if is_active[index]:
            # Mark the element as inactive
            is_active[index] = False
            
        # Increment step and update index
        step += 1
        index = (index + step) % total_elements  # Wrap around using modulus

    # Filter only the active elements
    active_elements = [element for element in is_active if element]

    # Output results based on the length of active_elements
    if len(active_elements) == 0:
        print("YES")  # All elements are inactive
    else:
        print("NO")   # There are still active elements

# Uncomment the following line to run the function
# process_elements()
