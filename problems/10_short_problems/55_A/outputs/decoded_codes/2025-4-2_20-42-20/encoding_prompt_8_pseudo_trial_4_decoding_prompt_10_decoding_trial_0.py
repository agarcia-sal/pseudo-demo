def can_all_positions_be_marked():
    # Step 1: Get input
    n = int(input())
    
    # Step 2: Initialize a boolean list
    positions = [True] * n
    
    # Step 3: Index variables
    current_index = 0
    step = 1
    
    # Step 4: Loop through positions
    while step <= 500000:
        if positions[current_index]:
            # Mark the current position as False
            positions[current_index] = False
        
        # Increment step and update current_index 
        step += 1
        current_index = (current_index + step) % n
    
    # Step 5: Check for unmarked positions
    unmarked_positions = [pos for pos in positions if pos]
    
    # Step 6: Output the result
    if len(unmarked_positions) == 0:
        print('YES')
    else:
        print('NO')

# Call the function
can_all_positions_be_marked()
