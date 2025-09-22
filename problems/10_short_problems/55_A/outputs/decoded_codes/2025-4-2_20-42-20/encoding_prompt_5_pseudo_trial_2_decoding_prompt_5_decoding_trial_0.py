def check_active_elements():
    # Retrieve the size of the list
    n = int(input())
    
    # Initialize the status list with all elements set to True
    status = [True] * n
    
    # Initialize index and increment variables
    index = 0
    increment = 1
    
    # Perform modifications based on the increment value
    while increment <= 500000:
        if status[index]:  # If the current element is active
            status[index] = False  # Mark it as inactive
        increment += 1  # Increase the increment value
        index = (index + increment) % n  # Update index with wrap-around
    
    # Check for remaining active elements
    active_elements = [element for element in status if element]
    
    # Determine and print the output based on the active elements
    if len(active_elements) == 0:
        print("YES")  # All elements are inactive
    else:
        print("NO")   # There are still active elements

# Uncomment the next line to call the function and run the program
# check_active_elements()
