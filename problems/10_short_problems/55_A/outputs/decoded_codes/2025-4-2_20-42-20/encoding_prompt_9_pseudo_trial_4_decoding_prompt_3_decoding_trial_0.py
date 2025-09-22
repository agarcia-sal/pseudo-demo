def process_boolean_list():
    # Step 1: Receive Input
    n = int(input())
    
    # Step 2: Initialize Variables
    boolean_list = [True] * n  # Create a list of n True values
    index = 0  # Current position in the list
    counter = 1  # Counter for the iterations

    # Step 3: Loop through a Range
    while counter <= 500000:
        if boolean_list[index]:  # Check if the current index is True
            boolean_list[index] = False  # Mark it as processed
        
        counter += 1  # Increment counter
        index = (index + counter) % n  # Update index with wrapping around if necessary

    # Step 4: Check for Remaining True Values
    remaining_true_values = [value for value in boolean_list if value]  # Collect all True values

    # Step 5: Determine Output
    if len(remaining_true_values) == 0:
        print("YES")  # All values have been processed
    else:
        print("NO")  # Some values remain True

# Test the function
process_boolean_list()
