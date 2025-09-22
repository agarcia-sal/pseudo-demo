# Function to determine the active status of the elements based on given steps
def check_active_elements():
    # Step 1: Input number of elements
    number_of_elements = int(input())
    
    # Step 2: Initialize a list with True values
    is_active = [True] * number_of_elements
    
    # Step 3: Initialize index and step variables
    index = 0
    step = 1

    # Step 4: While step is less than or equal to 500000
    while step <= 500000:
        # If the current index is active
        if is_active[index]:
            # Mark the index as inactive
            is_active[index] = False
        
        # Increment the step
        step += 1
        
        # Update the index (using modulo to cycle through the list)
        index = (index + step) % number_of_elements

    # Step 5: Create a list of active elements that are still True
    active_elements = [active for active in is_active if active]

    # Step 6: Check if there are any active elements remaining
    if len(active_elements) == 0:
        # If no active elements
        print('YES')
    else:
        # If there are active elements remaining
        print('NO')

# The function would be called here
check_active_elements()
