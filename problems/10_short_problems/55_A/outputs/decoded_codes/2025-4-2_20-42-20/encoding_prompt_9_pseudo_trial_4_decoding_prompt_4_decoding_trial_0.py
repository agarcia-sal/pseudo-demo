def process_boolean_list():
    # Step 1: Receive Input
    n = int(input())
    
    # Step 2: Initialize Variables
    boolean_list = [True] * n  # Create a list of True values of size n
    index = 0                   # Initialize index to track position in the list
    counter = 1                 # Initialize counter for iterations

    # Step 3: Loop through a Range
    while counter <= 500000:    # Continue looping while counter is less than or equal to 500,000
        if boolean_list[index]:  # Check if the current index is True
            boolean_list[index] = False  # Mark it as processed
        
        counter += 1            # Increment counter
        index = (index + counter) % n  # Update index, wrapping around with modulo

    # Step 4: Check for Remaining True Values
    remaining_true_values = [value for value in boolean_list if value]  # List of True values

    # Step 5: Determine Output
    if len(remaining_true_values) == 0:  # If no values are True
        print("YES")                     # Everything has been processed
    else:
        print("NO")                      # Some values are still True

# Call the function to execute
process_boolean_list()
