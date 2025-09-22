def main():
    # Read the integer input for the size of the array
    number_of_elements = int(input())
    
    # Initialize a boolean array with 'True' values for each index
    is_active = [True] * number_of_elements

    current_index = 0
    increment_value = 1

    # Loop until the increment value exceeds 500,000
    while increment_value <= 500000:
        # If the current index in the boolean array is still marked as active
        if is_active[current_index]:
            # Set the current index to inactive
            is_active[current_index] = False
        
        # Move to the next increment
        increment_value += 1
        
        # Update the current index using modulo operation to wrap around the boolean array
        current_index = (current_index + increment_value) % number_of_elements

    # Create a list of active indices based on the boolean array
    active_elements = [index for index, value in enumerate(is_active) if value]

    # Check if there are any active elements remaining
    if len(active_elements) == 0:
        print('YES')  # No active elements found
    else:
        print('NO')   # Active elements still present

# Call the main function to execute the program
if __name__ == "__main__":
    main()
