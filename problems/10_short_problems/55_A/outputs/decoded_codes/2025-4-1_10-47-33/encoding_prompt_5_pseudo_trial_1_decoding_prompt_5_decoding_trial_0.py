# Start the program
def marking_process():
    # Get the size of the boolean list from the user
    n = int(input())
    
    # Initialize a list with 'n' elements all set to True
    boolean_list = [True] * n
    
    # Set the initial index and increment
    index = 0
    increment = 1
    
    # WHILE increment is less than or equal to 500000
    while increment <= 500000:
        # IF the current position in boolean_list is True
        if boolean_list[index]:
            # Set the current position to False
            boolean_list[index] = False
        
        # Increase increment by 1
        increment += 1
        
        # Update the index, wrapping around using modulo n
        index = (index + increment) % n
    
    # Create a new list that contains all True values from boolean_list
    remaining_true = [value for value in boolean_list if value]
    
    # IF there are no True values left
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the process
marking_process()
