def find_smallest_integer():
    # Step 1: Get absolute input from the user
    target_sum = abs(int(input()))
    
    # Step 2: Initialize counter for the current index (integer evaluation)
    current_index = 0
    
    # Step 3: Loop indefinitely to find the appropriate integer
    while True:
        # Step 3a: Calculate the current sum of integers from 0 to current_index
        current_sum = current_index * (current_index + 1) // 2
        
        # Step 3b: Calculate the difference between current_sum and target_sum
        difference = current_sum - target_sum
        
        # Step 3c: Check for an exact match
        if current_sum == target_sum:
            print(current_index)
            break  # Terminate the loop if an exact match is found
        
        # Step 3d: Check if current_sum overshoots target_sum
        if current_sum > target_sum:
            if difference % 2 == 0:  # Check if the difference is even
                print(current_index)
                break  # Terminate the loop if current_index can adjust to match
        
        # Step 3e: Increment index for the next iteration
        current_index += 1

# Run the function
find_smallest_integer()
