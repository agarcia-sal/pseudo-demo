# Function to process the input as described in the pseudocode
def process_input():
    # Read an integer input for n
    n = int(input())
    
    # Initialize a boolean list of size n with all values set to True
    boolean_list = [True] * n

    # Initialize j and i
    j = 0
    i = 1

    # Loop until i exceeds 500000
    while i <= 500000:
        # If the current element in boolean_list at index j is True
        if boolean_list[j]:
            # Change the value at index j to False
            boolean_list[j] = False
        
        # Increment i by 1
        i += 1

        # Update j to the next index using modular arithmetic
        j = (j + i) % n

    # Create a new list from elements in boolean_list that are still True
    remaining_true = [value for value in boolean_list if value]

    # Check if there are no True values left in remaining_true
    if len(remaining_true) == 0:
        print('YES')  # All positions were marked False
    else:
        print('NO')   # There are still True positions left

# Call the function to execute
process_input()
