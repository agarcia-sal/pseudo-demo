def find_smallest_integer():
    # Step 1: Get Input
    target_sum = abs(int(input()))  # Read an integer from user input and calculate the absolute value
    
    # Step 2: Initialize Counter
    current_index = 0  # This will track the current integer being evaluated
    
    # Step 3: Loop Indefinitely
    while True:
        # Step 3a: Calculate Sum
        current_sum = current_index * (current_index + 1) // 2  # Sum of all integers from 0 to current_index
        
        # Step 3b: Difference Calculation
        difference = current_sum - target_sum  # Calculate the difference from target_sum
        
        # Step 3c: Check for Exact Match
        if current_sum == target_sum:
            print(current_index)
            break  # Terminate the loop
            
        # Step 3d: Check for Overshoot
        if current_sum > target_sum:
            if difference % 2 == 0:  # If the difference is even
                print(current_index)
                break  # Terminate the loop
                
        # Step 3e: Increment Index
        current_index += 1  # Move to the next integer

# Call the function to execute
find_smallest_integer()
