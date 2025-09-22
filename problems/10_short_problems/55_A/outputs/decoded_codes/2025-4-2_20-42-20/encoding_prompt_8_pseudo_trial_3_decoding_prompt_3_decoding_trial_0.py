def main():
    # Step 1: Get the total number of boolean elements from the user
    n = int(input())
    
    # Step 2: Create a list with n elements, all initially set to True
    boolean_list = [True] * n
    
    # Step 3: Initialize the current index and increment
    current_index = 0
    increment = 1
    
    # Step 4: Set the limit for increments
    limit = 500000
    
    # While the increment is within the specified limit
    while increment <= limit:
        # Check if the current position is still True
        if boolean_list[current_index]:
            # Set the current position to False
            boolean_list[current_index] = False
        
        # Update increment and current_index for the next iteration
        increment += 1
        current_index = (current_index + increment) % n  # Wrap around with modulo
    
    # Step 5: Create a list of remaining True values
    remaining_true = [value for value in boolean_list if value]
    
    # Step 6: Output result based on remaining True values
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Call the main function to run the code
main()
