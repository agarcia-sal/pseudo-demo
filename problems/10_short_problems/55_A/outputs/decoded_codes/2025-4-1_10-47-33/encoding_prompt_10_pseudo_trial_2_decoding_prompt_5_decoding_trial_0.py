def check_boolean_list():
    # Step 1: Input integer value n
    n = int(input())
    
    # Step 2: Initialize a list of boolean values
    boolean_list = [True] * n
    
    # Step 3: Initialize variables
    index_to_modify = 0
    i = 1
    
    # Step 4: Loop until i exceeds 500000
    while i <= 500000:
        
        # Step 5: Check if the current index in boolean_list is True
        if boolean_list[index_to_modify]:
            # Step 6: Set the current index to False
            boolean_list[index_to_modify] = False
            
        # Step 7: Increment i
        i += 1
        
        # Step 8: Update index_to_modify to the next index in a circular manner
        index_to_modify = (index_to_modify + i) % n
        
    # Step 9: Create a list of all True values in boolean_list
    true_values = [value for value in boolean_list if value]
    
    # Step 10: Check if there are no True values in true_values
    if len(true_values) == 0:
        # Step 11: Print 'YES' if no True values exist
        print('YES')
    else:
        # Step 12: Print 'NO' if True values exist
        print('NO')

# To test the function, uncomment the line below and provide an integer input.
# check_boolean_list()
