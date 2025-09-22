# Function to determine if all boolean values in a list can be set to False
def can_set_all_false():
    # Step 1: Read the number of elements
    number_of_elements = int(input())
    
    # Step 2: Initialize the boolean list with True values
    boolean_list = [True] * number_of_elements

    # Step 3: Initialize index and step
    index = 0
    step = 1

    # Step 4: Begin looping until step exceeds 500,000
    while step <= 500000:
        if boolean_list[index]:  # Check if the current position is True
            boolean_list[index] = False  # Mark the current position as False
        
        # Increment step for the next iteration
        step += 1
        
        # Update index, wrapping around using modulo
        index = (index + step) % number_of_elements

    # Step 5: Collect remaining True values
    remaining_true_values = [value for value in boolean_list if value]  # Filter for True values
    
    # Step 6: Determine the result based on the remaining values
    if len(remaining_true_values) == 0:
        print("YES")  # All values set to False
    else:
        print("NO")   # Some values remain True

# Note: The function can be called directly to execute the logic.
