# This function processes a boolean list based on specified conditions.
def process_boolean_list():
    # Step 1: Receive input for the size of the boolean list
    n = int(input())
    
    # Step 2: Initialize variables
    boolean_list = [True] * n  # Create a list of size n with all elements set to True
    index = 0                   # Initialize the current position in the list
    counter = 1                 # Start the counter at 1

    # Step 3: Loop through a range while counter is within limits
    while counter <= 500000:
        if boolean_list[index]:  # Check the current index
            boolean_list[index] = False  # Mark the position as processed
        counter += 1             # Increment the counter
        index = (index + counter) % n  # Update index with wrap around using modulo

    # Step 4: Check for remaining True values
    remaining_true_values = [value for value in boolean_list if value]

    # Step 5: Determine output based on the remaining true values
    if len(remaining_true_values) == 0:
        print("YES")  # All values have been processed
    else:
        print("NO")   # Some values remain True

# Call the function to execute the code
process_boolean_list()
