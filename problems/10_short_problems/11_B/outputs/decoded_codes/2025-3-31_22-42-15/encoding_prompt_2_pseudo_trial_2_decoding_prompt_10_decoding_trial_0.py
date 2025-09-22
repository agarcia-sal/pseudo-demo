def calculate_index_for_target_sum():
    # Step 2: Read an integer value from the user and store its absolute value
    target_sum = abs(int(input()))
    
    # Step 3: Initialize a counter
    index = 0
    
    while True:  # Step 4: Begin an infinite loop
        # Calculate the sum of the first 'index' natural numbers
        current_sum = index * (index + 1) // 2
        
        # Calculate the difference
        difference = current_sum - target_sum
        
        # Step 6: Check for exact match
        if current_sum == target_sum:
            print(index)  # Output the index
            break  # Exit the loop
        
        # Step 7: Check for overshoot
        if current_sum > target_sum:
            if difference % 2 == 0:  # Check if the difference is even
                print(index)  # Output the index
                break  # Exit the loop
        
        # Step 8: Increment the index
        index += 1

# Call the function to execute the logic
calculate_index_for_target_sum()
