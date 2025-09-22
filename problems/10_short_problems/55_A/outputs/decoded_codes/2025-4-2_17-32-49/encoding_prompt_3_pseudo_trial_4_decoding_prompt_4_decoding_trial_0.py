def main():
    # Step 1: Read the integer input for the size of the array
    number_of_elements = int(input())
    
    # Step 2: Initialize a boolean array with 'True' values for each index
    is_active = [True] * number_of_elements
    
    current_index = 0
    increment_value = 1

    # Step 3: Loop until the increment_value exceeds 500,000
    while increment_value <= 500000:
        # Step 4: Check if the current index in the boolean array is still marked as active
        if is_active[current_index]:
            # Set the current index to inactive
            is_active[current_index] = False
            
        # Move to the next increment
        increment_value += 1
        
        # Update the current index using modulo operation to wrap around the boolean array
        current_index = (current_index + increment_value) % number_of_elements

    # Step 5: Create a list of active indices based on the boolean array
    active_elements = [index for index, active in enumerate(is_active) if active]
    
    # Step 6: Check if there are any active elements remaining
    if len(active_elements) == 0:
        print('YES')  # No active elements found
    else:
        print('NO')   # Active elements still present

# Execute the main function
if __name__ == "__main__":
    main()
