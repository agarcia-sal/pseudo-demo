def mark_elements():
    # Step 2: Receive Input
    n = int(input())  # Read the size of the list
    
    # Step 3: Initialize Boolean List
    boolean_list = [True] * n  # Create a list of size n initialized to True
    
    # Step 4: Set Up Iteration Variables
    current_index = 0  # This will track the position in boolean_list
    step = 1  # This will dictate how far to move through the list during marking
    
    # Step 5: Mark Elements Process
    while step <= 500000:
        # Step 5.1: Check Current Position
        if boolean_list[current_index]:  # If the position is unmarked (True)
            boolean_list[current_index] = False  # Mark it as False (indicating it has been marked)
        
        # Step 5.2: Increment Step Value
        step += 1  # Increase the step value
        
        # Step 5.3: Calculate Next Position
        current_index = (current_index + step) % n  # Wrap around if exceeds list length
    
    # Step 6: Extract Remaining Unmarked Elements
    remaining_true = [value for value in boolean_list if value]  # List of unmarked elements (True)
    
    # Step 7: Check Results
    if len(remaining_true) == 0:  # If there are no unmarked positions left
        print("YES")  # Indicating all positions were marked
    else:
        print("NO")  # Indicating at least one position remained unmarked

# Call the function to execute the program
mark_elements()
