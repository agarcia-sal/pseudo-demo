# This program implements the described algorithm using Python.

def process_input_and_check():
    # Read input value for n (size of the boolean list)
    n = int(input())
    
    # Initialize a list of boolean values, all set to True
    boolean_list = [True] * n

    j = 0  # Initialize index for boolean_list
    i = 1  # Start incrementing i from 1

    # Loop until i exceeds 500000
    while i <= 500000:
        # If the current position in the list is True
        if boolean_list[j]:
            # Mark the position as False
            boolean_list[j] = False
            
        # Increment i
        i += 1
        
        # Update the index j in a circular manner
        j = (j + i) % n

    # Create a new list containing all elements from boolean_list that are True
    true_values_list = [value for value in boolean_list if value]

    # Check if there are any True values remaining
    if len(true_values_list) == 0:
        print('YES')
    else:
        print('NO')

# Call the function to execute the program
process_input_and_check()
