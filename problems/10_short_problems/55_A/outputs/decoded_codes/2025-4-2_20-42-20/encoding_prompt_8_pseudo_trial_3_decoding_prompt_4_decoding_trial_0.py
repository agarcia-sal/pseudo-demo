def main():
    # Step 1: Initialize input
    n = int(input())
    
    # Step 2: Create boolean list
    boolean_list = [True] * n
    
    # Step 3: Set initial positions
    current_index = 0
    increment = 1
    
    # Step 4: Update loop
    limit = 500000
    while increment <= limit:
        # If the current position in the boolean list is True, change it to False
        if boolean_list[current_index]:
            boolean_list[current_index] = False
        
        # Increment the step count
        increment += 1
        
        # Update current_index
        current_index = (current_index + increment) % n
    
    # Step 5: Check remaining True values
    remaining_true = [value for value in boolean_list if value]

    # Step 6: Output result
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Call the main function
main()
